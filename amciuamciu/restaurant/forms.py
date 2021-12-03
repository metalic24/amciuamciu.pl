
from .models import restaurant
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class Create_restaurant(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = [
            'name',
            'kitchen_type',
            'img_path',
            'street',
            'local_number',
            'city',
            'pass_code',
            
        ]
       

    def clean_name(self):
        name = self.cleaned_data.get("name")
        qs = restaurant.objects.filter(name = name)
        if qs.exists():
            raise forms.ValidationError("this restaurant name exists")
        
        return name

