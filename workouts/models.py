from django.conf import settings
from django.db import models


class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class WorkoutPlanExercise(models.Model):
    plan = models.ForeignKey(WorkoutPlan, related_name="exercises", on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=120)
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.exercise_name


class Workout(models.Model):
    WORKOUT_CHOICES = [
        ("gym", "Palestra"),
        ("bodyweight", "Corpo libero"),
        ("cardio", "Cardio"),
        ("mobility", "Mobilita"),
        ("other", "Altro"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(WorkoutPlan, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    workout_type = models.CharField(max_length=24, choices=WORKOUT_CHOICES, default="other")
    duration_minutes = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.get_workout_type_display()} - {self.date}"

    @property
    def total_volume_kg(self):
        total = 0
        for exercise in self.exercises.all():
            if exercise.weight_kg:
                total += float(exercise.weight_kg) * exercise.sets * exercise.reps
        return round(total, 2)


class ExerciseLog(models.Model):
    workout = models.ForeignKey(Workout, related_name="exercises", on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=120)
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.exercise_name

    @property
    def volume_kg(self):
        if not self.weight_kg:
            return 0
        return round(float(self.weight_kg) * self.sets * self.reps, 2)
