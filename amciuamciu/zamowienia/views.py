from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from restaurant.views import show_restaurants


from restaurant.models import restaurant as rest



def cart(request):
	context = {}
	return render(request, 'zamowienia/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'zamowienia/checkout.html', context)