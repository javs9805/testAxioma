from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class LoginForm(forms.Form):
    rut = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Rut Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Clave'}))