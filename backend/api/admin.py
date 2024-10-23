"""Файл для админ зоны."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Выводим нужные элементы."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
