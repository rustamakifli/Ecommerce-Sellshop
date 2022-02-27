from django.shortcuts import render

# Create your views here.

def order(request):
    return render(request,'order-complete.html')

def checkout(request):
    return render(request,'checkout.html')