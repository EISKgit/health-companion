from rest_framework import generics, permissions
from .models import Survey
from .serializers import SurveySerializer



class SurveyListCreateView(generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return surveys of the logged-in user
        return Survey.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Generate recommendation before saving
        data = serializer.validated_data
        recommendation = self.generate_recommendation(data)
        serializer.save(user=self.request.user, recommendation=recommendation)

    def generate_recommendation(self, data):
        tips = []

        if data.get("sleep_hours", 0) < 6:
            tips.append("😴 Try to get at least 7–8 hours of sleep.")

        if not data.get("ate_breakfast", True):
            tips.append("🍳 Skipping breakfast reduces energy. Have something healthy.")

        if data.get("water_glasses", 0) < 5:
            tips.append("💧 Drink at least 6–8 glasses of water today.")

        if data.get("activity_minutes", 0) < 30:
            tips.append("🏃 Try at least 20–30 minutes of physical activity.")

        if data.get("stress_level", 0) > 2:
            tips.append("🧘 High stress detected. Try breathing exercises or a short walk.")

        if data.get("screen_time", False):
            tips.append("📱 Avoid screens 1 hour before bed for better sleep.")

        if data.get("smoked_or_drink", False):
            tips.append("🚭 Avoid smoking/alcohol — it harms your long-term health.")

        if data.get("mood", 3) < 2:
            tips.append("😊 Try to do something relaxing or talk with a friend.")

        if data.get("work_hours", 0) > 10:
            tips.append("💻 Long work hours — remember to take breaks.")

        if data.get("pain", False):
            tips.append("🩺 You reported discomfort. Rest and monitor it.")

        if not tips:
            tips.append("🎉 Great job! Keep up your healthy habits.")

        return " ".join(tips)



class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow accessing own surveys
        return Survey.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Regenerate recommendation when updating survey
        data = serializer.validated_data
        recommendation = SurveyListCreateView.generate_recommendation(self, data)
        serializer.save(user=self.request.user, recommendation=recommendation)