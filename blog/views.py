from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from blog.forms import BlogCommentForm
# Create your views here.



def single_blog(request):
    form = BlogCommentForm()
    if request.method == 'POST':
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('single-blog'))


    context = {
        'form':form
    }
    return render(request,'single-blog.html',context)
   

def blog(request):
    return render(request,'blog.html')