from contextlib import ContextDecorator
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from blog.forms import BlogCommentForm
from blog.models import BlogBrand, BlogCategory,Blog,BlogComment
from django.views.generic import DetailView, CreateView, ListView


class BlogDetailView(DetailView, CreateView):
    template_name = 'single-blog.html'
    model = Blog
    context_object_name = 'blog'
    form_class = BlogCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['brands'] = BlogBrand.objects.all()
        context['blogs'] = Blog.objects.all()
        context['recents'] = Blog.objects.order_by("-created_at")
        cat_id = Blog.objects.get(slug=self.kwargs.get('slug')).category_id
        context['related_blogs'] = Blog.objects.filter(category__id=cat_id)
        context['comments'] = BlogComment.objects.filter(
            blog__slug=self.kwargs.get('slug')).all()
        context['comments_count'] = BlogComment.objects.filter(
            blog__slug=self.kwargs.get('slug')).all().count()
        return context

    def get_object(self):
        return Blog.objects.filter(slug=self.kwargs['slug']).first()


class BlogListView(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'
    ordering = ('-created_at', )
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