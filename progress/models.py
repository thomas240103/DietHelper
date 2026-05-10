from django.conf import settings
from django.db import models


class BodyProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    waist_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    chest_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hips_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Progressi - {self.date}"

