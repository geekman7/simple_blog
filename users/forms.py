from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','email','mobile','password1','password2']