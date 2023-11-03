# from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Editor


class EditorForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "E-Mail.."}), label="E-Mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password.."}),
        label="Password",
    )

    class Meta:
        model = Editor
        fields = ["email", "password"]
