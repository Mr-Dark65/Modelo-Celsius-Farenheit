"""Rutas de la app front."""
from django.urls import path

from . import views

app_name = "front"

urlpatterns = [
    path("", views.home, name="home"),
    path("api/predict/", views.predict, name="predict"),
]


