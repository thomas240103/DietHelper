from django import forms

from .models import BodyProgress


class BodyProgressForm(forms.ModelForm):
    class Meta:
        model = BodyProgress
        fields = ["date", "weight_kg", "waist_cm", "chest_cm", "hips_cm", "notes"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

