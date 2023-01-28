from rest_framework import serializers
from django.contrib.auth import get_user_model
from tasks.models import Task


class TaskSerializser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("pk", "tasker", "task", "date", "complete")
