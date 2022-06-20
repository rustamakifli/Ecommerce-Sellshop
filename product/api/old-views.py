from rest_framework.views import APIView
import django_filters.rest_framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)

from django.http import Http404
from rest_framework import filters
from product.api.serializers import ProductCreateSerializer,ProductReadSerializer
from product.models import ProductVersion

class CustomListCreateAPIView(ListCreateAPIView):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.request.method)

class ProductListCreateApi(CustomListCreateAPIView):
    queryset = ProductVersion.objects.all()
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,  filters.OrderingFilter)
    # filter_fields = ('category')
    serializer_classes = {
        'GET': ProductReadSerializer,
        'POST': ProductCreateSerializer
    }


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductCreateSerializer