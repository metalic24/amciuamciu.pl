from django.shortcuts import render
from .forms import  CreateUserForm

def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        form.save()

    context={
        'form':form
    }

    return render(request,"register.html",context)



def login(request):

   return  render(request,"login.html",{})
