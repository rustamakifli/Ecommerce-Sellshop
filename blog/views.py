from django.shortcuts import render

# Create your views here.



def single_blog(request):
    return render(request,'single-blog.html')