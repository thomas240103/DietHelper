from django.conf import settings
from django.db import models


class ShoppingItem(models.Model):
    CATEGORY_CHOICES = [
        ("fruit", "Frutta"),
        ("vegetables", "Verdura"),
        ("protein", "Proteine"),
        ("grains", "Cereali"),
        ("dairy", "Latticini"),
        ("other", "Altro"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=24, choices=CATEGORY_CHOICES, default="other")
    quantity = models.CharField(max_length=80, blank=True)
    is_bought = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["is_bought", "category", "name"]

    def __str__(self):
        return self.name

