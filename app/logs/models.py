from django.db import models
from django.utils.translation import gettext_lazy as _

from . import LogChoices


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

    class Meta:
        verbose_name = _("Logs")
        verbose_name_plural = _("Logs")
        ordering = ('-created_at', )
    
    def __str__(self):
        return self.method
