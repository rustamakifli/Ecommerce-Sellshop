from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import AddresForm, RegisterForm, LoginForm, CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def login_register(request):
    if not request.user.is_authenticated:
        reg_form = RegisterForm()
        login_form = LoginForm()
        next_page = request.GET.get('next','/')
        if request.method == 'POST':
            if request.POST.get('submit') == 'login':
                login_form = LoginForm(data=request.POST)
                if login_form.is_valid():
                    user = authenticate(email=login_form.cleaned_data['email'], password=login_form.cleaned_data['password'])
                    if user is not None:
                        django_login(request, user)
                        messages.add_message(request, messages.SUCCESS, 'You signed in!')
                        return redirect(next_page)        
                    else:
                        messages.add_message(request, messages.ERROR, 'Email or password is wrong!')
            elif request.POST.get('submit') == 'register':
                reg_form = RegisterForm(data=request.POST)
                if reg_form.is_valid():
                    user = reg_form.save()
                    user.set_password(reg_form.cleaned_data['password'])
                    user.save()
                    return redirect('/')
        context = {
                'reg_form': reg_form,
                'login_form':login_form,
            }
        return render(request, 'login-register.html', context)
    else:
        
        return redirect('/')

@login_required
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
def logout(request):
    django_logout(request)
    return redirect('/')

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'changepassword.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Ugurla sifreniz deyisdi')
        return super().get_success_url()

