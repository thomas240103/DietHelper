"""ASGI config for DietHelp."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diethelp.settings")

application = get_asgi_application()

