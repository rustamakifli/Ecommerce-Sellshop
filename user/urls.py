
from django.urls import path
from user.views import login_register, account, logout, user_profile

urlpatterns = [
    path('account/', account, name='account'),
    path('register/', login_register, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
]
