from django.http import HttpResponse
from django.shortcuts import  render


def carts(request):
    return render(request,'carts/cart.html')


def AllProducts(request):
    return render(request,'shop/products/list.html')
