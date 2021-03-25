from rest_framework import serializers

from logs.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ('created_at',)
        read_only_fields = ('id',)
