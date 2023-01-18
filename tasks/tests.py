from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # new
from .models import Task


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.task = Task.objects.create(
            task="new Task",
            tasker=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.task.tasker.username, "testuser")
        self.assertEqual(self.task.get_absolute_url(), "/")

    def test_url_exists_at_correct_location_listview(self):  # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):  # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_task.html")
