from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "birth_date",
            "height_cm",
            "starting_weight_kg",
            "current_weight_kg",
            "goal",
            "activity_level",
            "dietary_preferences",
            "allergies",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

