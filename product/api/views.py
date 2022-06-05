from requests import Response
from rest_framework.views import APIView
from product.api import serializers
from product.models import ProductVersion

class ProductListAPI(APIView):

    def get(self, request, *args, **kwargs):
        products = ProductVersion.objects.all()
        serializer = serializers.ProductVersionSerializer( products, many = True, context={'request': request})
        print(serializer.data)
        return Response(data=serializer.data)


# class ProductListView(ListView):
#     template_name = 'product-list.html'
#     model = ProductVersion
#     context_object_name = 'products'
#     paginate_by = 4
#     # ordering = ('created_at', )

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         category_id = self.request.GET.get('category_id') 
#         if category_id:
#             queryset = queryset.filter(category__id=category_id)
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['brands'] = Brand.objects.all()

#         return context