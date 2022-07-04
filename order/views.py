from django.shortcuts import render
# from order.models import Basket,BasketItem
import json
from product.models import ProductVersion
from django.http import JsonResponse
# Create your views here.
def wish(request):
    return render(request,'wishlist.html')
    
def cart(request):
 
    return render(request, 'cart.html')
	

def order(request):
    return render(request,'order-complete.html')

def checkout(request):
    return render(request,'checkout.html')

    

