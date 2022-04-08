from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from user.forms import AddresForm
# Create your views here.

# def login_register(request):
#     # form = RegisterForm()
#     # if request.method == 'POST':
#     #     form = RegisterForm(data=request.POST, files=request.FILES)
#     #     if form.is_valid():
#     #         user = form.save()
#     #         user.set_password(form.cleaned_data['password'])
#     #         user.save()
#     #         return redirect('/')
#     # context = {
#     #     'form': form
#     # }
#     return render(request, 'login.html', context)

def login(request):
    return render(request, 'login.html')

def account(request):
    form = AddresForm()
    if request.method == 'POST':
        form = AddresForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('account'))


    context = {
        'form':form
    }
    return render(request,'my-account.html',context)

