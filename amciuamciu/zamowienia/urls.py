from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:user_id>/<int:rest_id>/create/',views.create_zamowienie),
    # path('',views.show_zamowienie),
]
