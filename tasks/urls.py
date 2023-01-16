from django.urls import path
from .views import HomePage, AddTask, TaskDetailView, TaskEditView, TaskDeleteView

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("add/", AddTask.as_view(), name="add_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path("<int:pk>/edit/", TaskEditView.as_view(), name="edit_task"),
    path("<int:pk>/detail/", TaskDetailView.as_view(), name="detail_task"),
]
