from django.shortcuts import render
from .forms import Create_menu

from restaurant.models import restaurant as rest
def create_menu(request,rest_id):
    form = Create_menu(request.POST)
    restaurant = rest.objects.get(id = rest_id)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        instance = form.save(commit=False)
        instance.restaurant= restaurant
        instance.save()
        


    context={
        'form':form
    }
    
    
    return render(request,"menu/create_menu.html",context)