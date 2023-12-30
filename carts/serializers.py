from rest_framework import serializers
from .models import ShoppingCart, CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        # Extract 'cart_id' from the URL kwargs
        cart_id = self.context['view'].kwargs.get('cart_id')

        # Retrieve the ShoppingCart instance
        cart = ShoppingCart.objects.get(pk=cart_id)

        # Create the CartItem instance
        cart_item = CartItem.objects.create(cart=cart, **validated_data)
        return cart_item


class ShoppingCartSerializer(serializers.ModelSerializer):

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'
