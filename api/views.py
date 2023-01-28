from rest_framework import generics, viewsets
from tasks.models import Task
from rest_framework import permissions
from .serializer import TaskSerializser
from .permission import AuthorIsReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializser
    permission_classes = (AuthorIsReadOnly, permissions.IsAuthenticated)

    def get_queryset(self):
        return Task.objects.filter(tasker=self.request.user).order_by("-date")


class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializser
