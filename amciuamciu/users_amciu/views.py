from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

from zamowienia.models import Order, Ordered_Items
from .forms import  CreateUserForm
from restaurant.views import show_restaurants

def register(request):
    if request.user.is_authenticated:
        return redirect(show_restaurants)
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            new_user =form.save()
            login(request, new_user)
            return redirect(show_restaurants)

    context={
        'form':form
    }

    return render(request,"register.html",context)



def viev_login(request):

    
    context={
     
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(show_restaurants)
        else:
            messages.info(request,'Username or password is incorrect')
            return  render(request,"login.html",context)
  



    return  render(request,"login.html",context)

def hello_login(request):
    orders =[]
    user_orders = Order.objects.filter(customer = request.user.id)
    for order in user_orders:
        ordered_items = Ordered_Items.objects.filter(order = order)
        
      
          
            

    
    
   

    return render(request,"hello.html",{} )

def log_out(request):
    auth.logout(request)
    return redirect(show_restaurants)
    
    



#todo wylogowanie

#todo przekierowania
 