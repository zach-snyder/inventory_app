from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class Register(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        labels = {'first_name' : 'First Name', 'last_name' : 'Last Name', 'email' : 'Email', 'username' : 'Username', 'password' : 'Password'}

