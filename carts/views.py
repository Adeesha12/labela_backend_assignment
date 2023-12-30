from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ShoppingCart, CartItem
from .serializers import ShoppingCartSerializer, CartItemSerializer


class ShoppingCartListCreateView(generics.CreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart_id = self.kwargs.get('cart_id')
        cart = get_object_or_404(ShoppingCart, pk=cart_id)
        serializer.save(cart=cart)
