from django.db import models

import datetime
from django.utils import timezone


class Manufacturer(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    year = models.IntegerField(default=1990)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.model
