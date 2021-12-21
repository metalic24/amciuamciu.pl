from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from restaurant.views import show_restaurants
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from zamowienia.models import Ordered_Items, Order
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
@login_required(login_url='/users_amciu/login/')
def make_order(request):

	form = MakeOrder(request.POST)
	user = User.objects.get(username=request.user.username)
	
#	print("POST: ",request.POST)
	
	if request.method == 'POST':
		form_dic = {}	
		products_str = str(request.POST.get('objects'))
		products =json.loads(products_str)
		form_data = request.POST.get('form')
		form_data = json.loads(form_data)
		for form_d in form_data:
			form_dic[form_d['name']] = form_d['value']
		
		order = Order(customer = request.user, bill=0, street=form_dic['street'],
		building_number= form_dic['building_number'], local_number=form_dic['local_number'],
		city = form_dic['city'], pass_code=form_dic['pass_code'], 
		paid=False)
		order.save()
	#	for item in products.keys():
	#		print(products[item]['name'])

		
		for item in products.keys():
			order_item = Ordered_Items(order = order, menu_id= products[item]['id'],
			name= products[item]['name'], price = products[item]['price'], total_number = products[item]['in_cart']	
			)
			order_item.save()


	
					
		
    	

	context={
        'form': form
    }
	return render(request, 'zamowienia/make_order.html', context)
 