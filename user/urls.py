
from django.urls import path
from user.views import login, account

urlpatterns = [
    path('login/', login, name='login'),
    path('account/', account, name='account'),
]
