import datetime
import json

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


from . import LogChoices


class LogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_one_hour_stats(self):
        now = timezone.now()
        hour_ago = now - datetime.timedelta(days=1)
        
        stats_dict = {
            "GET": {
                "backgroundColor": "rgb(255, 99, 132)",
                "stats": []
            },
            "PUT": {
                "backgroundColor": "rgb(255, 159, 64)",
                "stats": []
            },
            "DELETE": {
                "backgroundColor": "rgb(255, 205, 86)",
                "stats": []
            },
            "POST": {
                "backgroundColor": "rgb(54, 162, 235)",
                "stats": []
            },
        }
        
        one_hour_requests = self.get_queryset().filter(
            created_at__lte=now,
            created_at__gte=hour_ago,
        )
        for request in one_hour_requests:
            
            stats_dict[request.method]["stats"].append({
                "x": str(request.created_at),
                "y": float(request.ms / 1000)
            })
        return stats_dict


class Log(models.Model):
    method = models.CharField(
        _("Method Type"),
        max_length=10,
        choices=LogChoices.CHOICES,
    )
    ms = models.PositiveSmallIntegerField(
        _("Request MS"),
    )
    timestamp = models.CharField(
        _("Timestamp"),
        max_length=30
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    
    objects = LogManager()

    class Meta:
        verbose_name = _("Logs")
        verbose_name_plural = _("Logs")
        ordering = ('-created_at', )
    
    def __str__(self):
        return self.method


@receiver(post_save, sender=Log)
def log_signal(sender, instance, created, **kwargs):
    if created:
        print("CREATED EQUAL TO TRUE")
        channel_layer = get_channel_layer()
        print("channel_layer:", channel_layer)
        print(instance)
        async_to_sync(channel_layer.group_send)(
            "gossip",
            {
                "type": "log.gossip",
                "event": "New Log",
                "data": Log.objects.get_one_hour_stats()
            },
        )
