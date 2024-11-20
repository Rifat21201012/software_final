from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from . import forms
from .models import Laptop


# Create your views here.
def add_laptops(request):
    if request.method == "GET":
        form = forms.LaptopForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('Add Successfully!')
    else:
        form = forms.LaptopForm()
    return render(request, 'forms.html', context={'form': form, })


def update_laptops(request, p_id):
    l = Laptop.objects.get(pk=p_id)
    if request.method == "GET":
        form = forms.LaptopForm(request.GET or None, instance=l)
        if form.is_valid():
            form.save()
            return HttpResponse('Update Successfully!')
    else:
        form = forms.LaptopForm(instance=l)
    return render(request, 'forms.html', context={'form': form, })


def delete_laptops(request, p_id):
    Laptop.objects.get(pk=p_id).delete()
    return HttpResponse('Deleted Successfully!')
