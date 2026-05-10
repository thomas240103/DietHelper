from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from pathlib import Path


def validate_activity_file(file):
    allowed = {".gpx", ".tcx", ".fit", ".csv"}
    suffix = Path(file.name).suffix.lower()
    if suffix not in allowed:
        raise ValidationError("Carica file GPX, TCX, FIT o CSV.")
    if file.size > 20 * 1024 * 1024:
        raise ValidationError("Il file corsa non deve superare 20 MB.")


class Run(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)
    duration_minutes = models.PositiveIntegerField()
    estimated_calories = models.PositiveIntegerField(blank=True, null=True)
    activity_file = models.FileField(
        upload_to="running/%Y/%m/",
        validators=[validate_activity_file],
        blank=True,
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    @property
    def average_pace(self):
        if not self.distance_km:
            return None
        total_minutes = float(self.duration_minutes)
        pace = total_minutes / float(self.distance_km)
        minutes = int(pace)
        seconds = round((pace - minutes) * 60)
        return f"{minutes}:{seconds:02d} min/km"

    def __str__(self):
        return f"{self.distance_km} km - {self.date}"


class RunTrackPoint(models.Model):
    run = models.ForeignKey(Run, related_name="track_points", on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    distance_km = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    elevation_m = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    seconds_from_start = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["index"]

    def __str__(self):
        return f"{self.run_id} - {self.distance_km} km"
