from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm ,SubscribeForm
from django.contrib import messages
from django.views.generic import CreateView

def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
    return render(request,'index.html')

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