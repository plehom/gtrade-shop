from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    cat = (
        ("Retrovizori","Retrovizori"),
        ("Farovi","Farovi"),
        ("Stopke","Stopke"),
        ("Gabariti","Gabariti"),
        ("Masine za injektore","Masine za injektore"),
        ("Sijalice","Sijalice"),
        ("Semerinzi","Semerinzi"),
        ("Zracni jastuci","Zracni jastuci"),
        ("Kocioni sistemi","Kocioni sistemi"),
        ("Dizel program","Dizel program"),
        ("Zracni ventili i reparacije","Zracni ventili i reparacije"),
        ("Crijeva za vodu","Crijeva za vodu"),
        ("Karoserija","Karoserija"),
        ("Hidraulika","Hidraulika"),
        ("Kompresori zraka","Kompresori zraka"),
        ("Grijanje i hladjenje","Grijanje i hladjenje"),
        ("Filteri","Filteri"),
        ("Ulje i maziva","Ulje i maziva"),
        ("Setovi kvacila","Setovi kvacila"),
        ("Dijelovi diferencijala i reduktora","Dijelovi diferencijala i reduktora"),
        ("Spojnice i prikljucci","Spojnice i prikljucci")
    )

    name = models.CharField( max_length=150)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.CharField(max_length=125,choices=cat, default="Farovi")
    image = models.ImageField(upload_to="uploads/")
    o = models.IntegerField(default=0)
    

class Cart(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,  on_delete=models.CASCADE)