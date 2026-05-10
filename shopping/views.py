from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ShoppingItem


@login_required
def shopping_home(request):
    items = ShoppingItem.objects.filter(user=request.user)
    return render(request, "shopping/home.html", {"items": items})

