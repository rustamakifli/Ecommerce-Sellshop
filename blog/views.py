from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from blog.forms import BlogCommentForm
from blog.models import BlogCategory,Blog
# Create your views here.

def single_blog(request):
    category = BlogCategory.objects.all()
    blog = Blog.objects.all()
    form = BlogCommentForm()
    if request.method == 'POST':
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('single-blog'))
    context = {
        'blogs':blog,
        'categories': category,
        'form':form,
        
    }
    return render(request,'single-blog.html',context)
   

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blogs':blog,
    }
    return render(request,'blog.html', context)