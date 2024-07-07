from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .forms import RegistrationForm,LoginForm,CreateProductForm
from django.http import HttpResponse
from .models import Product

# Create your views here.

class Index(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,"index.html",{"products":products})
class RegisterView(View):
    def get(self,request):
        form = RegistrationForm
        return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request):
        form = LoginForm
        return render(request,"login.html",{"form":form})

class ContactView(TemplateView):
    template_name = "contact.html"

class AdminCreateProduct(View):
    def get(self,request):
        form = CreateProductForm
        return render(request,"create.html",{"form":form})


class ShopView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,"shop.html",{"products":products})