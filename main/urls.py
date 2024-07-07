from django.urls import path 
from . import views

urlpatterns = [
    path("",views.Index.as_view(),name="home"),
    path("register/",views.RegisterView.as_view(),name="register"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("create/",views.AdminCreateProduct.as_view(),name="create"),
    path("shop/",views.ShopView.as_view(),name="shop")
]
