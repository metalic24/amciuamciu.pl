from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import restaurant
from .forms import Create_restaurant

from django.contrib.auth.decorators import login_required


@login_required(login_url='/users_amciu/login/')
def create_restaurant(request):
    form = Create_restaurant(request.POST, request.FILES)
    user = User.objects.get(username=request.user.username)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        instance = form.save(commit=False)
        instance.owner= user
        instance.save()
        return redirect(show_restaurants)


    context={
        'form':form
    }
    current_user = request.user
    
    return render(request,"restaurant/create_restaurant.html",context)

def show_restaurants(request):
    obj = restaurant.objects.all()
    objct = User.objects.all()

    context={"objs" : obj,
             "objcts" : objct
             }

    return render(request,"restaurant/show_restaurant.html",context)

@login_required(login_url='/users_amciu/login/')
def delete_restaurant(request,id):
    obj = get_object_or_404(restaurant, id=id)
    if request.user.id == obj.owner_id:
        if request.method == "POST":
            obj.delete()
        context={"objs" : obj}
    else:
         return  render(request,"restaurant",{})

    return render(request,"restaurant/delete_restaurant.html",context)
