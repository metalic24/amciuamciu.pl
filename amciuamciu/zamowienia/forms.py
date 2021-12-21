
from django import forms
from .models import Order

class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['street', 'building_number','local_number',
        'city', 'pass_code',
        ]

    