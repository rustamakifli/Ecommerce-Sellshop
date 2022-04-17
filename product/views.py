from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Category, ProductVersion, ProductReviews
from .forms import ProductReviewsForm
from django.http import Http404


def product(request):
    category_list = Category.objects.all()
    product_list = ProductVersion.objects.all()
    context = {
        'categories': category_list,
        'products': product_list
    }
    return render(request,'product-list.html', context)


def single_product(request, id=1):
    review_form = ProductReviewsForm()
    relatedproducts = ProductVersion.objects.all()
    singleproduct = ProductVersion.objects.get(id=id)
    product_reviews = ProductReviews.objects.all()
    product_colors = singleproduct.property.filter(property_name__name='color')
    product_sizes =  singleproduct.property.filter(property_name__name='size')
    
    if len(product_colors) == 0:
        product_colors = ['black', 'gray',]
    if len(product_sizes) == 0:
        product_sizes = ['s', 'm',]

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

