from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Category, ProductVersion
from .forms import ProductReviewsForm
from django.http import Http404

# Create your views here.

def product(request):
    category_list = Category.objects.all()
    product_list = ProductVersion.objects.all()
    context = {
        'categories': category_list,
        'products': product_list
    }
    return render(request,'product-list.html', context)

def single_product(request):
    review_form = ProductReviewsForm()
    related_products = ProductVersion.objects.all()
    if request.method == 'POST':
        review_form = ProductReviewsForm(data=request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse_lazy('single_product'))
        else:
            raise Http404 
    context = {
        'review_form':review_form,
        'related_products': related_products,
        'products': related_products,
        }
    return render(request,'single-product.html', context)
