from django import forms

from .models import ExerciseLog, Workout, WorkoutPlan


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["date", "plan", "workout_type", "duration_minutes", "notes"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["plan"].queryset = WorkoutPlan.objects.filter(user=user)
        self.fields["plan"].required = False
        self.fields["plan"].empty_label = "Nessuna scheda salvata"


class ExerciseLogForm(forms.ModelForm):
    class Meta:
        model = ExerciseLog
        fields = ["exercise_name", "sets", "reps", "weight_kg"]


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ["name", "description"]


class ExerciseBulkForm(forms.Form):
    exercises = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Panca piana, 4, 8, 60\nSquat, 4, 6, 80\nTrazioni, 3, 8",
            }
        ),
        help_text="Formato: esercizio, serie, ripetizioni, kg opzionali. Una riga per esercizio.",
    )
