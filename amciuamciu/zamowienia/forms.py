from .models import zamowienia
from django import forms


class Create_zamowienie(forms.ModelForm):
    class Meta:
        model = zamowienia
        fields = [
            'danie',
            'cena',
            'email',
            'telefon',
            'ulica',
            'budynek',
            'mieszkanie',
        ]