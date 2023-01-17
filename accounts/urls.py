from django.urls import path
from .views import SignupView, CLoginView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", CLoginView.as_view(), name="login"),
]
