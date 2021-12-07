from django.urls import path,include
from . import views

urlpatterns = [
  path('<int:rest_id>/create/',views.create_menu),
  
]
