from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="surveys",
        null=True,
        blank=True
    )

    # Core fields
    sleep_hours = models.FloatField(default=0)
    ate_breakfast = models.BooleanField(default=False)
    water_glasses = models.IntegerField(default=0)
    activity_minutes = models.IntegerField(default=0)
    stress_level = models.IntegerField(default=0)
    screen_time = models.FloatField(default=0)  # in hours
    mood = models.IntegerField(default=3)  # 1=low, 5=high
    smoked_or_drink = models.BooleanField(default=False)
    work_hours = models.IntegerField(default=0)
    pain = models.BooleanField(default=False)

    # System-generated
    recommendation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"Survey by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"
        return f"Survey (Guest) on {self.created_at.strftime('%Y-%m-%d')}"
