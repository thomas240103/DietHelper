from django.contrib import admin

from .models import ExerciseLog, Workout, WorkoutPlan, WorkoutPlanExercise


class WorkoutPlanExerciseInline(admin.TabularInline):
    model = WorkoutPlanExercise
    extra = 1


class ExerciseLogInline(admin.TabularInline):
    model = ExerciseLog
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "plan", "workout_type", "duration_minutes")
    list_filter = ("workout_type", "date")
    inlines = [ExerciseLogInline]


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "updated_at")
    search_fields = ("name", "user__username")
    inlines = [WorkoutPlanExerciseInline]
