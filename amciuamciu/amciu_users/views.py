from django.shortcuts import render

def registration(request):
    context ={}

    render(request, "register.html",context)
