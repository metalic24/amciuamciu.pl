from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import menu
from .forms import Create_menu

from restaurant.models import restaurant as rest

@login_required(login_url='/users_amciu/login/')
def create_menu(request,rest_id):
    form = Create_menu(request.POST, request.FILES)
    restaurant = rest.objects.get(id = rest_id)
    if request.user.id == restaurant.owner.id:
        
        if form.is_valid():
            name = form.cleaned_data.get("name")
            instance = form.save(commit=False)
            instance.restaurant= restaurant
            instance.save()

        context={
            'form':form
        }
    
        return render(request,"menu/create_menu.html",context)
    else:
        return render(request, "restaurant/nope.html",{})

def show_menu(request, rest_id):
    objs = menu.objects.filter(restaurant_id = rest_id)

    context = {
        'objs':objs,
    }
    return render(request,"menu/show_menu.html",context)
