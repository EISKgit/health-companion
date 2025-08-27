from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Survey

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ["username", "email", "age", "gender", "location"]

class SurveySerializer(serializers.ModelSerializer):
    breakfast = serializers.BooleanField(source="ate_breakfast")
    water = serializers.IntegerField(source="water_glasses")
    activity = serializers.IntegerField(source="activity_minutes")
    stress = serializers.IntegerField(source="stress_level")
    substance_use = serializers.BooleanField(source="smoked_or_drink")
    pain_details = serializers.CharField(source="pain_notes", allow_blank=True, required=False)

     # Add recommendation explicitly
    recommendation = serializers.CharField(read_only=True)


    class Meta:
        model = Survey
        fields = [
            "id", "user", "date",
            "sleep_hours", "energy", "breakfast", "water",
            "activity", "stress", "screen_time", "mood",
            "substance_use", "work_hours", "pain", "pain_details", "weather_effect","recommendation",
        ]
        read_only_fields = ["user", "date"]

