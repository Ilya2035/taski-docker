"""Серилизатор."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Значения для модели."""

    class Meta:
        """Указываем только мету."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
