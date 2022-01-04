from django.urls import path,include
from . import views

urlpatterns = [
   path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
   path('make_order/', views.make_order, name="make_order"),
   path('pay/<int:id>/', views.pay_for_order, name="pay_for_order"),
]
