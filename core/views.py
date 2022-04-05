from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
