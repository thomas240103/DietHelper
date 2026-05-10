from django.urls import path

from . import views


urlpatterns = [
    path("", views.shopping_home, name="shopping_home"),
]

