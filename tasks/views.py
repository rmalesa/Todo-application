from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import AddForm
from .models import Task


class HomePage(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.filter(tasker=self.request.user).order_by("-date")


class AddTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "edit_add_task.html"
    form_class = AddForm

    def form_valid(self, form):
        form.instance.tasker = self.request.user
        form.instance.task = form.instance.task.capitalize()
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    template_name = "detail_task.html"

    def post(self, requrst, *args, **kwargs):
        task = self.get_object()
        task.complete = True
        task.save()
        return redirect(reverse_lazy("home"))

    def test_func(self):
        object = self.get_object()
        return object.tasker == self.request.user


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "delete_task.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        object = self.get_object()
        return object.tasker == self.request.user


class TaskEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = "edit_add_task.html"
    form_class = AddForm

    def test_func(self):
        object = self.get_object()
        return object.tasker == self.request.user
