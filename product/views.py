from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Category, ProductVersion, ProductReviews
from .forms import ProductReviewsForm
from django.http import Http404
from django.contrib import messages
from django.views.generic import DetailView,CreateView
from django.views.generic import ListView


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
    # ordering = ('created_at', )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def single_product(request, id=1):
    review_form = ProductReviewsForm()
    relatedproducts = ProductVersion.objects.all()
    singleproduct = ProductVersion.objects.get(id=id)
    product_reviews = ProductReviews.objects.all()
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
    model = ProductReviews
    template_name = 'single-product.html'
    form_class = ProductReviewsForm
    # success_url = reverse_lazy('product')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
        return result

    def get_object(self):
        return ProductVersion.objects.filter(id=self.kwargs['pk']).first()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = ProductVersion.objects.all()

        context['review_form'] = ProductReviewsForm(data=self.request.POST)
        context['reviews'] = ProductReviews.objects.all()
        context['product'] = self.get_object()
        context['colors'] = self.get_object().property.filter(property_name__name='color')
        context['sizes'] = self.get_object().property.filter(property_name__name='size')
    

        return context
