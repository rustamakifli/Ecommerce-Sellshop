from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Brand, Category, ProductVersion, ProductReview, Product, Color, Size
from .forms import ProductReviewsForm
from django.http import Http404,JsonResponse
from django.contrib import messages
from django.views.generic import DetailView,CreateView
from django.views.generic import ListView
import json
from order.models import *
from django.db.models import Max, Min

# def product(request):
#     category_list = Category.objects.all()
#     product_list = ProductVersion.objects.all()
#     context = {
#         'categories': category_list,
#         'products': product_list
#     }
#     return render(request,'product-list.html', context)

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
        color_id = self.request.GET.get('color_id') 
        size_id = self.request.GET.get('size_id') 
        max_price = self.request.GET.get('max_price') 
        min_price = self.request.GET.get('min_price') 
        if category_id:
            # not work
            queryset = queryset.filter(category__id=category_id)
        if brand_id:
            # not work
            queryset = queryset.filter(brand__id=brand_id)
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

# def single_product(request, id=1):
#     review_form = ProductReviewsForm()
#     relatedproducts = ProductVersion.objects.all()
#     singleproduct = ProductVersion.objects.get(id=id)
#     product_reviews = ProductReview.objects.all()
#     product_colors = singleproduct.property.filter(property_name__name='color')
#     product_sizes =  singleproduct.property.filter(property_name__name='size')
#     if request.method == 'POST':
#         review_form = ProductReviewsForm(data=request.POST)
#         if review_form.is_valid():
#             review_form.save()
#             return redirect(reverse_lazy('single_product', kwargs={"id": singleproduct.id}))
#         else:
#             raise Http404 
#     context = {
#         'review_form':review_form,
#         'related_products': relatedproducts,
#         'product': singleproduct,
#         'colors' : product_colors,
#         'sizes' : product_sizes,
#         'reviews' : product_reviews,
#         }
#     return render(request,'single-product.html', context)


class ProductView(DetailView,CreateView):
    model = ProductReview
    template_name = 'single-product.html'
    form_class = ProductReviewsForm
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
        context['colors'] = self.get_object().property.filter(property_name__name='color')
        context['sizes'] = self.get_object().property.filter(property_name__name='size')
    

        return context

def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)
        customer = request.user
        product = ProductVersion.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse("item was added",safe=False )