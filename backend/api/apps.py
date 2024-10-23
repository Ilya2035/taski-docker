"""Прописываем приложение для основы."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Приложение без спецнастройки."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
