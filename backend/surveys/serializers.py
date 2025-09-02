from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"
        read_only_fields = ["id", "created_at", "recommendation", "user"]
