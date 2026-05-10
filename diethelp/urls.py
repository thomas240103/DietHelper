from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("nutrition/", include("nutrition.urls")),
    path("shopping/", include("shopping.urls")),
    path("documents/", include("documents.urls")),
    path("workouts/", include("workouts.urls")),
    path("running/", include("running.urls")),
    path("progress/", include("progress.urls")),
    path("ai/", include("ai_assistant.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

