from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField, DecimalField, EmailField
from django.db.models.fields.related import ForeignKey, ForeignObject
from menu.models import menu

from restaurant.models import restaurant as rest

CHOISES = {

    ('przyjete', 'przyjete'),
    ('oplacone', 'oplacone'),
    ('przygotowywane', 'przygotowywane'),
    ('dostarczne', 'dostarczane'),
    ('zakonczone', 'zakonczone')
}




class Order(models.Model):
    customer = ForeignKey(User, on_delete=CASCADE)
    bill = DecimalField( max_digits=6,decimal_places=2)
    date = DateTimeField(auto_now_add=True)
    street = CharField(max_length=150, null=False)
    building_number = IntegerField(null=False)
    local_number = IntegerField(null=True)
    city = CharField(max_length=150, null=False)
    pass_code = IntegerField(null=False)
    paid = BooleanField(default=False)
    status = CharField(max_length=20, choices=CHOISES , default='przyjete')
    rest = ForeignKey(rest, on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)

    #todo
    #status zamówienia

class Ordered_Items(models.Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    menu_id = IntegerField()
    name = CharField(max_length=150)
    price = DecimalField(max_digits=5, decimal_places=2)
    total_number = IntegerField()


