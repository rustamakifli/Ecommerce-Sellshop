from django.shortcuts import render
from product.models import Category
# Create your views here.
def product(request):
    category_list = Category.objects.all()
    # sub_category_list = {}
    # for each in category_list:
    #     sub_category_list [each] = []
    #     subcategories = Category.objects.filter (parent_cat= each.id).order_by('mysweetchild')
    #     for subcat in subcategories:
    #         sub_category_list[each].append(subcat)
    context = {
        'categories': category_list,
        # 'sub_category': sub_category_list
    }
    return render(request,'product-list.html',context)

def single_product(request):
    return render(request,'single-product.html')