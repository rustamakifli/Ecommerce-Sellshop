from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Category, ProductVersion, ProductReviews
from .forms import ProductReviewsForm
from django.http import Http404

# from webcolors import name_to_rgb
# def Color(name):
#   return name_to_rgb(name)[::-1] 


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
    product_colors = ['green', 'black', 'white']
    product_sizes = ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl', '4xl']
    product_reviews = ProductReviews.objects.all()
    # colors = []
    # for i in product_colors:
    #     i = Color(i)
    #     colors.append(i)
    if request.method == 'POST':
        review_form = ProductReviewsForm(data=request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse_lazy('single_product', kwargs={"id": 1}))
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

