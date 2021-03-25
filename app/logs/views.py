from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from logs.models import Log
from logs.serializers import LogSerializer


class LogListAPIView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
