from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DecimalField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

from restaurant.models import restaurant as rest



class menu(models.Model):
    name = CharField(null=False,max_length=120)
    restaurant = ForeignKey(rest, on_delete=CASCADE, null=False)
    price = DecimalField(max_digits=20, decimal_places=2, null=False)
    description = TextField(null=True)
    img_path = models.ImageField(upload_to='images/')



