from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from user.forms import AddresForm, RegisterForm, LoginForm


def login_register(request):
    reg_form = RegisterForm()
    log_form = LoginForm()
    if request.method == 'POST':
        log_form = LoginForm(data=request.POST)
        reg_form = RegisterForm(data=request.POST)
        if log_form.is_valid():
            user = log_form.save()
            return redirect(reverse_lazy('account'))
        if reg_form.is_valid():
            user = reg_form.save()
            user.set_password(reg_form.cleaned_data['password'])
            user.save()
            return redirect('/')
    context = {
        'form': reg_form,
        'log_form' : log_form
    }
    return render(request, 'login.html', context)


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

