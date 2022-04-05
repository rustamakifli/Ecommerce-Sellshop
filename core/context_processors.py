from .forms import ContactForm, SubscribeForm
from django.http import Http404
from django.contrib import messages

def contact_renderer(request):
    contact_form = ContactForm()
    if request.method == 'POST' and 'contact' in request.POST:
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact qeyde alindi!')
        else:
            raise Http404 
    context = {
        'contact_form':contact_form
        }
    return context

def subscribe_renderer(request):
    print("1")
    subscribe_form = SubscribeForm()
    if request.method == 'POST' and 'subscribe' in request.POST:
        print("2")
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            print("3")
            subscribe_form.save()
            messages.add_message(request, messages.SUCCESS, 'Email qeyde alindi!')
        else:
            print("4")
            raise Http404 
    context = {
        'subscribe_form':subscribe_form
        }
    return context