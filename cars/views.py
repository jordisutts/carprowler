# 1 Create the cars app inside our project
# 1 python3 manage.py startapp cars
# 1 You can have multiple apps in your project
# 1 Now we will create a view

from django.http import HttpResponse

from .models import Car

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    all_cars_list = Car.objects.all()

    context = {
        'all_cars_list': all_cars_list,
    }

    return render(request, 'cars/index.html', context)


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/detail.html', {'car': car})
