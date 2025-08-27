from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="surveys", null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    sleep_hours = models.IntegerField(null=True, blank=True)       # Q1
    energy = models.IntegerField(null=True, blank=True)            # Q2 (scale 1–3)
    ate_breakfast = models.BooleanField(null=True, blank=True)     # Q3
    water_glasses = models.IntegerField(null=True, blank=True)     # Q4
    activity_minutes = models.IntegerField(null=True, blank=True)  # Q5
    stress_level = models.IntegerField(null=True, blank=True)      # Q6 (scale 1–3)
    screen_time = models.BooleanField(null=True, blank=True)       # Q7
    mood = models.IntegerField(null=True, blank=True)              # Q8 (scale 1–5)
    smoked_or_drink = models.BooleanField(null=True, blank=True)   # Q9
    work_hours = models.IntegerField(null=True, blank=True)        # Q10
    pain = models.BooleanField(null=True, blank=True)              # Q11
    pain_notes = models.TextField(null=True, blank=True)           # optional
    weather_effect = models.CharField(max_length=20, null=True, blank=True)  # Q12

        # New field
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.user:
            return f"Survey by {self.user.username} on {self.date}"
        return f"Survey (no user) on {self.date}"

