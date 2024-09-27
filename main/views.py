from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from django.views import View
from .forms import RegistrationForm,LoginForm,CreateProductForm
from django.http import HttpResponse
from .models import Product,Cart,CartItem,Order
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login

from django.contrib.postgres.search import SearchVector

from .forms import UploadExcelForm
import pandas as pd



# Create your views here.

class Index(View):
    def get(self,request):
        print(request.user)
        products = Product.objects.all()
        return render(request,"index.html",{"products":products})

class RegisterView(View):
    def get(self,request):
        form = RegistrationForm
        return render(request,"register.html",{"form":form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("login")
        else:
            return render(request,"register.html",{"form":form,"invalid":"Pogresan unos. Pokusajte ponovo"})


class LoginView(View):
    def get(self,request):
        form = LoginForm
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("USLO")
                print(user)
                login(request,user)
                cart = Cart.objects.filter(usr=user).first()
                if cart is None:
                    c = Cart.objects.create(usr=user)
                    c.save()
                return redirect("home")
            else:
                print("greska1",user)
                return render(request,"login.html",{"form":form,"invalid":"Uneseni podaci nisu tacni !"})
        else:
            return render(request,"login.html",{"form":form,"invalid":"Uneseni podaci nisu tacni !"})

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
    def post(self,request):
        response = Product.objects.filter(oem=request.POST["search"])
        print(request.POST["search"])
        return render(request,"shop.html",{"products":response})

class ProductDetailView(DetailView):
    model = Product
    template_name="product_detail.html"
    ##### POST DIO GDJE SE DODAJE U CART ITEM
    def post(self,request,pk):
        cart = Cart.objects.filter(usr=request.user).first()
        pr = Product(id=pk)
        item = CartItem.objects.create(cart=cart,item=pr)
        item.save()
        return redirect("home")

class CartView(View):
    suma = 0
    def get(self,request):
        cart = Cart.objects.filter(usr=request.user).first()
        items = CartItem.objects.filter(cart=cart)
        for i in items:
            self.suma = self.suma + i.item.price
        print(items)
        
        return render(request,"cart.html",{"items":items,"suma":self.suma})
    def post(self,request):
        item = CartItem.objects.get(id=request.POST["id"])
        item.delete()

        cart = Cart.objects.filter(usr=request.user).first()
        items = CartItem.objects.filter(cart=cart)
        for i in items:
            self.suma = self.suma + i.item.price
        return render(request,"cart.html",{"items":items,"suma":self.suma})

##class OrderView(View):
    ##def post(self,request):
        
class CategoryListingView(View):
    def get(self,request,cat):
        products = Product.objects.filter(category=cat)
        return render(request,"category.html",{"products":products})


def upload_excel(request):
    if request.method == "POST":
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            
            # Učitavanje Excel datoteke koristeći Pandas
            df = pd.read_excel(excel_file)
            
            # Iteriranje kroz redove i spašavanje u bazu
            for _, row in df.iterrows():
                Product.objects.create(
                    name=row['B'],
                    description=row['B'],
                    price=5,
                    fabric=row['C']
                )
                
            return redirect('success')  # ili gdje želiš redirektovati nakon uspješnog spašavanja
    else:
        form = UploadExcelForm()

    return render(request, 'upload_excel.html', {'form': form})

