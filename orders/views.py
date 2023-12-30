from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Delivery
from .serializers import DeliverySerializer, OrderItemSerializer, OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OrderItemCreateView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class DeliveryCreateView(generics.CreateAPIView):
    serializer_class = DeliverySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
