from django.contrib import admin

from .models import Run


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "distance_km", "duration_minutes", "average_pace")
    list_filter = ("date",)

