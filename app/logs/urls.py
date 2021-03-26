from django.urls import path

from logs.views import (
    LogListAPIView,
    LogPostAPIView,
)


app_name = "logs"

urlpatterns = [
    path('', LogListAPIView.as_view(), name="list"),
    path('detail/', LogPostAPIView.as_view(), name="post")
]
