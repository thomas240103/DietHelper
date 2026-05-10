from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "goal", "activity_level", "current_weight_kg")
    search_fields = ("user__username", "user__email")

