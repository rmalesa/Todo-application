from django.urls import path, include
from rest_framework.authtoken import views
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("task", TaskViewSet, basename="task")


urlpatterns = [
    path("", include(router.urls)),
    #     path("", TaskAPIView.as_view()),
    #     path("<int:pk>/", TaskAPIDetailView.as_view()),
    path("api-token/", views.obtain_auth_token),
]
