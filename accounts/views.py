from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserLoginForm, CustomSignUpForm


class SignupView(CreateView):
    form_class = CustomSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class CLoginView(LoginView):
    authentication_form = CustomUserLoginForm
