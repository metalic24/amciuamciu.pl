from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from restaurant.views import show_restaurants
from .forms import Create_zamowienie

from restaurant.models import restaurant as rest

# Create your views here.
def create_zamowienie(request, user_id, rest_id):
    form = Create_zamowienie(request.POST)
    user = User.objects.get(id = user_id)
    restaurant = rest.objects.get(id = rest_id)
    
    if form.is_valid():
        name = form.cleaned_data.get("name")
        instance = form.save(commit=False)
        instance.zamawiajacy = user
        instance.restauracja = restaurant
        instance.save()
        return redirect(show_restaurants)
    
    context={
        'form':form
    }
    
    current_user = request.user
    
    return render(request, "zamowienia/create_zamowienie.html", context)