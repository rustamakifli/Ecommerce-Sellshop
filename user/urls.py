
from django.urls import path
from user.views import account, login_register,logout, ChangePasswordView

urlpatterns = [
    path('account/', account, name='account'),
    path('register/', login_register, name='register'),
    path('login/', login_register, name='login'),
    path('logout/', logout, name='logout'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
