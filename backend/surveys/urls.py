from django.urls import path
from .views import SurveyListCreateView, SurveyDetailView

urlpatterns = [
    path("", SurveyListCreateView.as_view(), name="survey-list-create"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="survey-detail"),
]
