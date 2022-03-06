
from django.urls import path
from user.views import login, account, contact

urlpatterns = [
    path('login/', login, name='login'),
    path('account/', account, name='account'),
    path('contact/', contact, name='contact'),
]
