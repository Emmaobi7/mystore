from django.urls import path
from .import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]