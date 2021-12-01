from django.contrib.auth.models import User
from django.shortcuts import render
from .models import restaurant
from .forms import Create_restaurant



def create_restaurant(request):
    form = Create_restaurant(request.POST)
    user = User.objects.get(username=request.user.username)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        instance = form.save(commit=False)
        instance.owner= user
        instance.save()

    context={
        'form':form
    }
    current_user = request.user
    
    return render(request,"restaurant/create_restaurant.html",context)