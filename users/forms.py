from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # a meta class is a class that holds information about
    # here, the RegisterForm class
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
