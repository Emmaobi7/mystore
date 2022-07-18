from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    just_arrived = Product.objects.filter(just_arrived=True)
    trandy = Product.objects.filter(trandy=True)
    top_selling = Product.objects.filter(top_selling=True)
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'top_selling':top_selling,
        'trandy':trandy,
        'just':just_arrived,
    }
    return render(request, 'store/index.html', context)



def shop(request):
    all = Product.objects.all()
    context = {
        'all':all,
    }
    return render(request, 'store/shop.html', context)



def detail(request, pk):
    detail = Product.objects.get(id=pk)
    context = {
        'detail':detail,
    }
    return render(request, 'store/detail.html', context)

