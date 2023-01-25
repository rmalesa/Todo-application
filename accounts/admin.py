from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomSignUpForm, CustomUserLoginForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomSignUpForm
    list_display = [
        "username",
        "email",
        "profile_pic",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("profile_pic",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("profile_pic",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
