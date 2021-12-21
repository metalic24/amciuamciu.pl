from django.contrib import admin

from .models import Order, Ordered_Items

admin.site.register(Ordered_Items)
admin.site.register(Order)



