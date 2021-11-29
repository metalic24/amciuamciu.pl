
from django.urls import path, include
from . import views

urlspattern = [
    path("register/", views.registration, name="register"),
]