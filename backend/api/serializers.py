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
    class Meta:
        model = Survey
        exclude = ["user"]   # user will be set automatically