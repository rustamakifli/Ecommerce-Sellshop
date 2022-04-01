from django.shortcuts import render
from product.models import Category,ProductVersion
# Create your views here.
def product(request):
    category_list = Category.objects.all()
    product_list = ProductVersion.objects.all()
    context = {
        'categories': category_list,
        'products': product_list
    }
    return render(request,'product-list.html',context)

def single_product(request):
    return render(request,'single-product.html')