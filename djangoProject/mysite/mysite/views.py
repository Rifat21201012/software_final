from django.shortcuts import render
from laptops.models import Laptop


def home(request):
    laptops = Laptop.objects.all()
    return render(request, 'home.html', context={'laptops': laptops})
