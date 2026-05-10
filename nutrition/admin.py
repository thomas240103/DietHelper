from django.contrib import admin

from .models import Food, Meal, MealItem


class MealItemInline(admin.TabularInline):
    model = MealItem
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "calories_per_100g", "protein_per_100g", "carbs_per_100g", "fat_per_100g")
    search_fields = ("name",)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "meal_type")
    list_filter = ("meal_type", "date")
    inlines = [MealItemInline]

