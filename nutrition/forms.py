from django import forms

from .models import Food, Meal, MealItem


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "calories_per_100g", "protein_per_100g", "carbs_per_100g", "fat_per_100g"]


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["date", "meal_type", "notes"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}


class MealItemForm(forms.ModelForm):
    class Meta:
        model = MealItem
        fields = ["food", "quantity_g"]

