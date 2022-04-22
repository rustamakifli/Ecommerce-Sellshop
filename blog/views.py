from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from blog.forms import BlogCommentForm
from blog.models import BlogCategory,Blog
from django.views.generic import ListView

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
   

# def blog(request):
#     blog = Blog.objects.all()
#     context = {
#         'blogs':blog,
#     }
#     return render(request,'blog.html', context)


class BlogListView(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'
    ordering = ('created_at', )
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') 
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        return context