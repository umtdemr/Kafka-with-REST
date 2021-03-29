from django.urls import path

from logs.views import (
    LogsView,
    LogListAPIView,
    LogPostAPIView,
)


app_name = "logs"

urlpatterns = [
    path('', LogsView.as_view(), name="stats"),
    path('api/', LogListAPIView.as_view(), name="list"),
    path('api/detail/', LogPostAPIView.as_view(), name="post")
]
