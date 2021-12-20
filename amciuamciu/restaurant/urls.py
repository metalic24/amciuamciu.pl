from django.urls import path,include
from . import views

urlpatterns = [
  path('create/',views.create_restaurant),
  path('<int:id>/delete/',views.delete_restaurant),
  path('',views.show_restaurants),
]
