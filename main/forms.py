from django import forms 
from django.forms import TextInput,PasswordInput,EmailInput
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["first_name","last_name","username","email","password1","password2"]
        widgets ={
            'first_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'',
            }),
            'last_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'',
            }),
            'username':TextInput(attrs={
                'class':'form-control',
                'placeholder':'',
            }),
            'email':EmailInput(attrs={
                'class':'form-control',
                'placeholder':""
            }),
            'password':PasswordInput(attrs={
                'class':'form-control',
                'placeholder':''
            })
        }

class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'username':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username',
            }),
            'password':PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'password'
            })
        }

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","price","category","image"]

class UploadExcelForm(forms.Form):
    file = forms.FileField()
        