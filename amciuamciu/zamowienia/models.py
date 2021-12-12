from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField, DecimalField, EmailField
from django.db.models.fields.related import ForeignKey, ForeignObject

from restaurant.models import restaurant as rest

# Create your models here.

class zamowienia(models.Model):
    zamawiajacy = models.ForeignKey(User, on_delete=CASCADE, null=False)    
    restauracja = models.ForeignKey(rest, on_delete=CASCADE, null=False)
    danie = TextField()
    cena = DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    email = EmailField(max_length=254, null=False, default='email')
    telefon = DecimalField(max_digits=9, decimal_places=0, null=False, default='0')
    ulica = CharField(max_length=120, null=False)
    budynek =CharField(max_length=10, null=False)
    mieszkanie =DecimalField(max_digits=5, decimal_places=0, default='0')
    
