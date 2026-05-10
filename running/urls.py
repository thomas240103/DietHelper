from django.urls import path

from . import views


urlpatterns = [
    path("", views.running_home, name="running_home"),
]

