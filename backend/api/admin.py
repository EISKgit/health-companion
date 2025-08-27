from django.contrib import admin
from .models import Survey

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "mood", "sleep_hours", "energy")  # remove stress if not a field
    list_filter = ("date", "mood")  # only keep actual fields
    search_fields = ("user__username",)

