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
        # Attach survey to logged-in user
        serializer.save(user=self.request.user)


class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow accessing own surveys
        return Survey.objects.filter(user=self.request.user)
