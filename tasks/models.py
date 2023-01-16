from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Task(models.Model):
    tasker = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(max_length=255, null=True)
    complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy("home")

    def __str__(self):
        return self.task
