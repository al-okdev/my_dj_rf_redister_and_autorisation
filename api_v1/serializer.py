from rest_framework import serializers

from api_v1.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['user', 'title', 'text', 'status', 'created_at']

        # поля только для чтения
        read_only_fields = ['user']