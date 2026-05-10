from django.contrib import admin

from .models import BodyProgress


@admin.register(BodyProgress)
class BodyProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "weight_kg", "waist_cm")
    list_filter = ("date",)

