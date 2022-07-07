from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from product.models import Brand, Category, ProductImage, ProductVersion, ProductReview, Product, Color, Size, ProductImage, Tag
from .forms import ProductReviewsForm
from django.http import Http404,JsonResponse
from django.contrib import messages
from django.views.generic import DetailView,CreateView
from django.views.generic import ListView
import json
from django.template.defaulttags import register

from order.models import *
from django.db.models import Max, Min, Count

# filter by price
min_price = ProductVersion.objects.all().aggregate(Min('new_price'))
max_price = ProductVersion.objects.all().aggregate(Max('new_price'))

class ProductListView(ListView):
    template_name = 'product-list.html'
    model = ProductVersion
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') 
        brand_id = self.request.GET.get('brand_id') 
        tag_id = self.request.GET.get('tag_id') 
        color_id = self.request.GET.get('color_id') 
        size_id = self.request.GET.get('size_id') 
        max_price = self.request.GET.get('max_price') 
        min_price = self.request.GET.get('min_price') 
        if category_id:
            queryset = queryset.filter(product__category__id=category_id)
        if brand_id:
            queryset = queryset.filter(product__brand__id=brand_id)
        if tag_id:
            queryset = queryset.filter(product__tag__id=tag_id)
        if color_id:
            queryset = queryset.filter(color__id=color_id)
        if size_id:
            queryset = queryset.filter(size__id=size_id)
        if min_price:
            queryset = queryset.filter(new_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(new_price__lte=max_price)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        context['min_price'] = float(min_price.get('new_price__min'))
        context['max_price'] = float(max_price.get('new_price__max')
)
        return context


class ProductView(DetailView,CreateView):
    model = ProductVersion
    template_name = 'single-product.html'
    context_object_name = 'product'
    form_class = ProductReviewsForm
    success_url = reverse_lazy('product')

    def form_valid(self, form):
        form.instance.product_version_id = self.kwargs['pk']
        form.instance.user = self.request.user
        star = self.request.POST.get("star_value",None)
        form.instance.rating = star
        return super().form_valid(form)


    def get_object(self):
        return ProductVersion.objects.filter(id=self.kwargs['pk']).first()

    def get_success_url(self):
        productid = self.kwargs['pk']
        return reverse_lazy('single_product', kwargs = {'pk':productid})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_product = self.get_object()
        parent_product = single_product.product

        context['related_products'] = ProductVersion.objects.filter(
            product__category=ProductVersion.objects.get(pk=self.kwargs.get('pk')).product.category).exclude(pk=self.kwargs.get('pk'))[0:3]
        context['review_form'] = ProductReviewsForm(
            data=self.request.POST)
        context['reviews'] = ProductReview.objects.filter(
            product_version_id=self.kwargs.get('pk')).all()
        context['images'] = ProductImage.objects.filter(
            product_version=self.kwargs.get('pk'))[0:4]
        context['product_versions_query'] = ProductVersion.objects.filter(
            product__id=parent_product.id)
        context['product_version_tags'] = Tag.objects.filter(
            product__id=parent_product.id
        )
        return context
