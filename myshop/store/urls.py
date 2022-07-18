from django.urls import path
from .import views


app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('detail/<int:pk>', views.detail, name='detail'),
]