from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    # to take the input of username
    username = forms.CharField(max_length=100)
    # to take the input of email
    email = forms.CharField(max_length=100)

