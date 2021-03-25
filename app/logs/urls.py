from django.urls import path

from logs.views import LogListAPIView


app_name = "logs"

urlpatterns = [
    path('', LogListAPIView.as_view(), name="list")
]
