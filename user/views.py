from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from user.forms import AddresForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_register(request):
    reg_form = RegisterForm()
    log_form = LoginForm()
    next_page = request.GET.get('next', '/')
    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            log_form = LoginForm(data=request.POST)
            if log_form.is_valid():
                user = authenticate(email=log_form.cleaned_data['email'], password=log_form.cleaned_data['password'])
                if user is not None:
                    django_login(request, user)
                    return redirect(next_page)
                else:
                    messages.add_message(request, messages.ERROR, 'Username or password incorrect!')
        elif request.POST.get('submit') == 'register':
            reg_form = RegisterForm(data=request.POST)
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

@login_required
def user_profile(request):
    return render(request, 'my-account.html')

@login_required
def logout(request):
    django_logout(request)
    return redirect('/')