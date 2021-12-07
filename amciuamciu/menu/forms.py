
from .models import menu
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class Create_menu(forms.ModelForm):
    class Meta:
        model = menu
        fields = [
            'name',
            'description',
            'price',
            
        ]
       

    def clean_name(self):
        name = self.cleaned_data.get("name")
        qs = menu.objects.filter(name = name)
        if qs.exists():
            raise forms.ValidationError("this dish  name exists")
        
        return name

