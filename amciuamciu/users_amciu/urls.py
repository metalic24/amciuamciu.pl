from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register),
    path('hello/',views.hello_login),

    path('login/',views.viev_login),
    path('log_out/',views.log_out),
    path('hello/users_orders',views.users_orders, name= "users-orders"),
    path('hello/users_orders/details/<int:id>',views.user_order_details, name= "users-orders-details"),
    path('hello/restaurants/',views.users_restaurants, name= "users-restaurants"),
    path('hello/restaurants/orders/<int:id>',views.restaurants_orders, name= "restaurant-orders"),
     path('hello/restaurant/orders/details/<int:id>',views.restaurant_order_details, name= "restaurant-orders-details"),
]
