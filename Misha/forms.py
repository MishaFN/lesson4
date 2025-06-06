from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Regform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LogForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']