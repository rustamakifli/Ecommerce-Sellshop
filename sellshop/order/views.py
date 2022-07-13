from django.shortcuts import render
# from order.models import Basket,BasketItem
from django.http.response import HttpResponseRedirect
from order.models import User,ShippingAddress,Basket,Order
from product.models import ProductVersion
from django.http import JsonResponse
from order.forms import ShippingAddressForm
from django.views.generic.base import View
# Create your views here.
def wish(request):
    return render(request,'wishlist.html')
    
def cart(request):
    return render(request, 'cart.html')
	

def order(request):
    return render(request,'order-complete.html')

# def checkout(request):
    
#     return render(request,'checkout.html')

class CheckoutShipping(View):
    template_name = 'checkout.html'
    http_method_names = ['get', 'post']


    def get(self, request):
        form = ShippingAddressForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            
            form.save()
         
            return HttpResponseRedirect('/checkout')
        else:
            return render(request, 'checkout.html', {'form': form})



class CheckoutConfirm(View):
    template_name = 'checkout-confirm.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)