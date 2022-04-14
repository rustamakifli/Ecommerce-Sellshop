
from django.urls import path
from user.views import login_register, account

urlpatterns = [
    path('account/', account, name='account'),
    path('register/', login_register, name='login'),
]
