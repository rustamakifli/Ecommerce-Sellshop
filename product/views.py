from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Brand, Category, ProductVersion, ProductReview,Product,ProductImage,Color,Size
from .forms import ProductReviewsForm
from django.http import Http404,JsonResponse
from django.contrib import messages
from django.views.generic import DetailView,CreateView
from django.views.generic import ListView
import json
from django.template.defaulttags import register

from order.models import *

def product(request):
    category_list = Category.objects.all()
    product_list = ProductVersion.objects.all()
    context = {
        'categories': category_list,
        'products': product_list
    }
    return render(request,'product-list.html', context)


class ProductListView(ListView):
    template_name = 'product-list.html'
    model = ProductVersion
    context_object_name = 'products'
    paginate_by = 4

    # ordering = ('created_at', )

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') 
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        # context['products'] = ProductVersion.objects.all()
        return context


def single_product(request, id=1):
    review_form = ProductReviewsForm()
    relatedproducts = ProductVersion.objects.all()
    singleproduct = ProductVersion.objects.get(id=id)
    product_reviews = ProductReview.objects.all()
    product_colors = singleproduct.property.filter(property_name__name='color')
    product_sizes =  singleproduct.property.filter(property_name__name='size')
    if request.method == 'POST':
        review_form = ProductReviewsForm(data=request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse_lazy('single_product', kwargs={"id": singleproduct.id}))
        else:
            raise Http404 
    context = {
        'review_form':review_form,
        'related_products': relatedproducts,
        'product': singleproduct,
        'colors' : product_colors,
        'sizes' : product_sizes,
        'reviews' : product_reviews,
        }
    return render(request,'single-product.html', context)


class ProductView(DetailView,CreateView):
    model = ProductVersion
    template_name = 'single-product.html'
    form_class = ProductReviewsForm
    context_object_name = 'detailed'
    # success_url = reverse_lazy('product')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
        return result

    def get_object(self):
        return ProductVersion.objects.filter(id=self.kwargs['pk']).first()

    def get_success_url(self):
        productid = self.kwargs['pk']
        return reverse_lazy('single_product', kwargs = {'pk':productid})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = ProductVersion.objects.all()
        context['review_form'] = ProductReviewsForm(data=self.request.POST)
        context['reviews'] = ProductReview.objects.all()
        context['product'] = self.get_object()
        # context['products'] = ProductVersion.objects.get(quantity=6)
        # context['colors'] = self.get_object().property.filter(property_name__name='color')
        # context['sizes'] = self.get_object().property.filter(property_name__name='size')
    

        return context

    
    @register.filter
    def get_range(value):
        if value < 6:
            return range(1, value+1)
        return range(1, 6)

