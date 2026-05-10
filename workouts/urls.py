from django.urls import path

from . import views


urlpatterns = [
    path("", views.workouts_home, name="workouts_home"),
    path("scheda/<int:plan_id>/usa/", views.start_plan_workout, name="start_plan_workout"),
    path("scheda/<int:plan_id>/elimina/", views.delete_plan, name="delete_plan"),
]
