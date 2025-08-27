from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
import json
from .serializers import SurveySerializer
from rest_framework import status


def health_check(request):
    return JsonResponse({"status": "ok", "message": "API is working!"})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SurveyView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    
    def get(self, request):
        surveys = request.user.surveys.all().order_by("-date")
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            recommendation = self.generate_recommendation(data)

            # Pass recommendation to serializer.save()
            serializer.save(
                user=request.user if request.user.is_authenticated else None,
                recommendation=recommendation
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def generate_recommendation(self,data):
        tips = []

        if data.get("sleep_hours", 0) < 6:
            tips.append("You slept less than 6 hours 😴. Try to go to bed earlier tonight.")

        if not data.get("breakfast", True):
            tips.append("You skipped breakfast 🍳. Eating in the morning helps boost energy.")

        if data.get("water", 0) < 4:
            tips.append("You drank less water 💧. Aim for at least 6-8 glasses today.")

        if data.get("activity", 0) < 30:
            tips.append("You had low activity yesterday 🏃. Try a 20-minute walk.")

        if data.get("stress", 0) > 2:
            tips.append("You reported high stress 😟. Take 10 mins for deep breathing or meditation.")

        if data.get("screen_time", False):
            tips.append("You used screens before bed 📱. Try avoiding screens 1h before sleep.")

        if data.get("substance_use", False):
            tips.append("Avoid smoking/alcohol 🚭. It affects your long-term health.")

        if data.get("mood", 2) < 2:
            tips.append("Your mood seems low 😔. Do something relaxing that you enjoy today.")

        if data.get("work_hours", 0) > 10:
            tips.append("Long work/study hours 🖥️. Remember to take short breaks.")

        if data.get("pain", False):
            tips.append("You reported discomfort 🩺. Make sure to rest and track it daily.")

        if not tips:
            tips.append("Great job! Keep up your healthy habits 🎉")

        return " ".join(tips)
def perform_create(self, serializer):
        data = serializer.validated_data.copy()  # copy validated data
        recommendation = SurveyView().generate_recommendation(data)  # generate tips
        print("here -> ",recommendation)
        serializer.save(user=self.request.user, recommendation=recommendation)
