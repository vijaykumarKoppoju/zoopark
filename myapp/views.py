from django.shortcuts import render
from .models import Animals,Category
# Create your views here.
from django.http import *
from django.urls import reverse

def mainpage(req):
    return render(req,"myapp/mainPage.html")

def homepage(req):
    
    return render(req,"myapp/home.html")

def ticketspage(req):
    return render(req,'myapp/tickets.html')

def paymentpage(req):
    return render(req,"myapp/payment.html")

def aboutpage(req):
    return render(req,"myapp/about.html")

def animals_page(req):
    category=Category.objects.get(title="animals")
    animal = Animals.objects.filter(category="animals")
    return render(req,"myapp/animals.html",{"animals":animal,"info":category})

def bird_page(req):

    category=Category.objects.get(title="birds")
    animal = Animals.objects.filter(category="birds")
   
    return render(req,"myapp/animals.html",{"animals":animal,"info":category})

def reptile_page(req):
    category=Category.objects.get(title="reptiles")
    animal = Animals.objects.filter(category="reptiles")
    
    return render(req,"myapp/animals.html",{"animals":animal,"info":category})

def aquatic_page(req):
    
    category=Category.objects.get(title="aquatics")
    animal = Animals.objects.filter(category="aquatics")
    return render(req,"myapp/animals.html",{"animals":animal,"info":category})

def animal_detail(req,name):

    animal = Animals.objects.get(slug=name)
    cate=animal.category
    path=cate
    return render(req,"myapp/specificanimal.html",{"animal":animal ,"page":path})