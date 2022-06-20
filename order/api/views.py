from rest_framework import permissions,status
from order.models import Order,OrderItem
from order.api.serializers import OrderSerializer,OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class OrderView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = Order.objects.get(user=request.user.customer)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderItemView(APIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        Order.objects.get_or_create(user=request.user.customer, is_ordered=False)
        obj = OrderItem.objects.filter(
            cart=Order.objects.get(user=request.user.customer, is_ordered=False)).order_by('created_at')
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)