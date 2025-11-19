"""Configuración de la app front."""
from django.apps import AppConfig


class FrontConfig(AppConfig):
    """Configuración de la app front."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "front"
    verbose_name = "Front TensorFlow.js"


