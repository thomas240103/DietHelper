from django.contrib import admin

from .models import ShoppingItem


@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "category", "quantity", "is_bought")
    list_filter = ("category", "is_bought")
    search_fields = ("name", "user__username")

