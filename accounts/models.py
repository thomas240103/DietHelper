from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    GOAL_CHOICES = [
        ("weight_loss", "Dimagrimento"),
        ("maintenance", "Mantenimento"),
        ("muscle_gain", "Massa muscolare"),
        ("performance", "Performance"),
    ]

    ACTIVITY_CHOICES = [
        ("low", "Bassa"),
        ("medium", "Media"),
        ("high", "Alta"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    height_cm = models.PositiveIntegerField(blank=True, null=True)
    starting_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    current_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    goal = models.CharField(max_length=32, choices=GOAL_CHOICES, blank=True)
    activity_level = models.CharField(max_length=16, choices=ACTIVITY_CHOICES, blank=True)
    dietary_preferences = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profilo di {self.user}"

