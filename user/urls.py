
from django.urls import path
from user.views import login, account,register

urlpatterns = [
    path('account/', account, name='account'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),

]
