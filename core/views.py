from django.shortcuts import redirect, render
from .forms import ContactForm, SubscribeForm
from django.http import Http404
from django.contrib import messages


def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact qeyde alindi!')
        else:
            raise Http404
        return redirect('/')
    context = {
        'contact_form':contact_form
        }
    return render(request,'contact.html', context)

def subscribe_renderer(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.add_message(request, messages.SUCCESS, 'Email qeyde alindi!')
        else:
            raise Http404 
        return redirect('/')
    context = {
        'subscribe_form':subscribe_form
        }
    return render(request,'index.html', context)