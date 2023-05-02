from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets

from tasks.models import Task

from .permission import AuthorIsReadOnly
from .serializer import TaskSerializser


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializser
    permission_classes = (AuthorIsReadOnly, permissions.IsAuthenticated)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["complete"]

    def get_queryset(self):
        return Task.objects.filter(tasker=self.request.user).order_by("-date")


class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializser
