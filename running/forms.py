from django import forms

from .models import Run


class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ["date", "distance_km", "duration_minutes", "estimated_calories", "activity_file", "notes"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}
