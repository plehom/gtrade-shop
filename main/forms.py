from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","price","category","image"]