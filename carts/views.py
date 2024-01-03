from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingCart, CartItem
from .serializers import ShoppingCartSerializer, CartItemSerializer


# class ShoppingCartListCreateView(ListCreateAPIView):
#     queryset = ShoppingCart.objects.all()
#     serializer_class = ShoppingCartSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return ShoppingCart.objects.filter(user_id=user)
    
#     def perform_create(self, serializer):
#         user = self.request.user
#         cart = user.shoppingcart_set.first()
#         if not cart:
#             cart = ShoppingCart.objects.create(user_id=user)
#         serializer.save(user_id=user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# class CartItemCreateView(CreateAPIView):
#     serializer_class = CartItemSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         cart_id = self.kwargs.get('cart_id')
#         cart = get_object_or_404(ShoppingCart, pk=cart_id)
#         serializer.save(cart=cart,user=self.request.user)


class CartItemCreateView(CreateAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart_id = self.kwargs.get('cart_id')
        cart = get_object_or_404(ShoppingCart, pk=cart_id)
        serializer.save(cart=cart, user=self.request.user)

class CartItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        return CartItem.objects.filter(cart_id=cart_id)