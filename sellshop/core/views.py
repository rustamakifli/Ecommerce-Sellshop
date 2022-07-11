from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm ,SubscribeForm
from django.contrib import messages
from django.views.generic import CreateView
from product.models import ProductImage,ProductVersion
from blog.models import Blog
from django.db.models import Count


def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
    new_arrivals = ProductVersion.objects.order_by("-created_at")
    mostreview = ProductVersion.objects.annotate(
        num_rev=Count('product_reviews')).order_by('-num_rev')[:6]
    bestseller = ProductVersion.objects.annotate(
        mostsold=Count('Product_Cart')).order_by('-mostsold')[1:8]
    firstbestseller = ProductVersion.objects.annotate(
        mostsold=Count('Product_Cart')).order_by('-mostsold')[0] if ProductVersion.objects.count() > 0 else None
    latest_blog = Blog.objects.order_by("-created_at")[:3]
    images = ProductImage.objects.filter(is_main=True)
    productversions = ProductVersion.objects.all()
    context = {
        'title': 'Home Sellshop',
        'mostreview': mostreview,
        'new_arrivals': new_arrivals,
        'latest_blog': latest_blog,
        'images': images,
        'bestseller': bestseller,
        'firstbestseller': firstbestseller,
        'productversions': productversions,
    }

    return render(request,'index.html',context=context)

# def contact(request):
#     contact_form = ContactForm()
#     if request.method == 'POST':
#         contact_form = ContactForm(data=request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             messages.add_message(request, messages.SUCCESS, 'Contact qeyde alindi!')
#         else:
#             raise Http404
#         return redirect(reverse_lazy('index'))
#     context = {
#         'contact_form':contact_form
#         }
#     return render(request,'contact.html', context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
        return result



# def subscribe_renderer(request):
#     subscribe_form = SubscribeForm()
#     if request.method == 'POST':
#         subscribe_form = SubscribeForm(data=request.POST)
#         if subscribe_form.is_valid():
#             subscribe_form.save()
#             messages.add_message(request, messages.SUCCESS, 'Email qeyde alindi!')
#         else:
#             raise Http404 
#         return redirect(reverse_lazy('index'))
#     context = {
#         'subscribe_form':subscribe_form
#         }
#     return render(request,'index.html', context)

class SubscribeView(CreateView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Email qeyde alindi!')
        return result