
from django.urls import path
from core.views import about, error404, index

urlpatterns = [
    path('about/', about, name='about'),
    path('error404/', error404, name='error404'),
    path('', index, name='index'),
]
