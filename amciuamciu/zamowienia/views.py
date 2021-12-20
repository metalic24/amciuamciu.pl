from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from restaurant.views import show_restaurants
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from zamowienia.models import Ordered_Items
from .forms import MakeOrder
import json



from restaurant.models import restaurant as rest



def cart(request):
	context = {}
	return render(request, 'zamowienia/cart.html', context)


def checkout(request):
	
	if request.method == 'POST':
		objects = request.POST.get('objects','')
		

	context = {}
	return render(request, 'zamowienia/checkout.html', context)

def make_order(request):

	form = MakeOrder(request.POST)
	user = User.objects.get(username=request.user.username)

	if form.is_valid() and request.method == 'POST':
		
		instance = form.save(commit=False)
		instance.customer = user
		instance.bill = 0
		form.save()

		
    	

	context={
        'form': form
    }
	return render(request, 'zamowienia/make_order.html', context)
 