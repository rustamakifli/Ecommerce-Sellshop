from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import AddresForm, RegisterForm,LoginForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def login(request):
    form = LoginForm()
    next_page = request.GET.get('next','/')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                messages.add_message(request, messages.SUCCESS, 'You signed in!')
                return redirect(next_page)        
            else:
                messages.add_message(request, messages.ERROR, 'Email or password is wrong!')
    context = {
        'login_form':form,
    }
    return render(request, 'login.html', context)

@login_required
def user_profile(request):
    return render(request, 'my-account.html')

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

