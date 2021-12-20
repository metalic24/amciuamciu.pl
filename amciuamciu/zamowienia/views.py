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
	items =[]
	print(request.POST)
	if request.method == 'POST':
			
			if request.POST.get('objects') != None:
				products_str = request.POST.get('objects')
				products = json.loads(products_str)
				for key in products.keys():
					dic={}
					
					for key2 in products[key].keys():
						dic[key2] = products[key][key2]
						
					items.append(dic)
	



	if form.is_valid() and request.method == 'POST':
		
	
		instance = form.save(commit=False)
		instance.customer = user
		instance.bill = 0
		order =	form.save()
		
			
		
		for item in items:
			ordered_item= Ordered_Items(
				order = order,
				menu_id = item['id'],
				name = item['name'],
				price = item['price'],
				total_number = item['in_cart']
				
			)
			print(item)
			
			ordered_item.save()


		

		
			
	
	
	

		
		
    	

	context={
        'form': form
    }
	return render(request, 'zamowienia/make_order.html', context)
 