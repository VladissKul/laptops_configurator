from django.http import HttpResponse
from django.shortcuts import render

from .models import Laptop


def home(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptop_shop/home.html', {'laptops': laptops})


def gamer_laptop(request):
    laptops = Laptop.objects.filter(is_gaming=True)
    return render(request, 'laptop_shop/gamer_laptop.html', {'laptops': laptops})


def os_laptop(request):
    laptops = Laptop.objects.filter(os=True)
    return render(request, 'laptop_shop/os_laptop.html', {'laptops': laptops})
