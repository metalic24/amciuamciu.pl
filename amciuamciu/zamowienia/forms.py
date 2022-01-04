
from django import forms
from django.db.models import fields
from .models import Order

class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['street', 'building_number','local_number',
        'city', 'pass_code',
        ]

class UpdateStatus(forms.ModelForm):
    class Meta: 
        model = Order
        fields = ['status']
    