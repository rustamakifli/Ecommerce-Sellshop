from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def account(request):
    return render(request,'my-account.html')