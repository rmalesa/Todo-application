from django import forms
from .models import Task


class AddForm(forms.ModelForm):
    task = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter Your Task",
                "class": "sumthg",
            }
        )
    )

    class Meta:
        model = Task
        fields = ("task",)
