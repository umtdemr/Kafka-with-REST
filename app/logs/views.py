import json

from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from logs.models import Log
from logs.serializers import LogSerializer
from logs.logger import write_log, wait_random


class LogListAPIView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    
    def get(self, *args, **kwargs):
        waited_ms = wait_random()
        write_log('GET', waited_ms)
        return super().get(*args, **kwargs)


class LogPostAPIView(APIView):
    def post(self, *args, **kwargs):
        waited_ms = wait_random()
        write_log('POST', waited_ms)
        return Response(
            {"detail": "post log has writed"}
        )

    def put(self, *args, **kwargs):
        waited_ms = wait_random()
        write_log('PUT', waited_ms)
        return Response(
            {"detail": "put log has writed"}
        )

    def delete(self, *args, **kwargs):
        waited_ms = wait_random()
        write_log('DELETE', waited_ms)
        return Response(
            {"detail": "delete log has writed"}
        )


class LogStatsView(View):
    def get(self, *args, **kwargs):
        return JsonResponse(Log.objects.get_one_hour_stats())


class LogsView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stats"] = json.dumps(Log.objects.get_one_hour_stats())
        context["all_stats"] = Log.objects.all()
        return context
    
