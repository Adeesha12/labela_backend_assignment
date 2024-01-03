from rest_framework import serializers

from products.models import Product
from .models import ShoppingCart, CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'created_at']

    def create(self, validated_data):
          # Extract 'cart_id' from the URL kwargs
        cart_id = self.context['view'].kwargs.get('cart_id')

        # Retrieve the ShoppingCart instance
        cart = ShoppingCart.objects.get(pk=cart_id)

        # Extract product data from validated_data
        product_data = validated_data.pop('product')

        # Retrieve or create the Product instance
        product_serializer = ProductSerializer(data=product_data)
        product_serializer.is_valid(raise_exception=True)
        product = product_serializer.save()

        # Create the CartItem instance
        cart_item = CartItem.objects.create(cart=cart, product=product, **validated_data)
        return cart_item


class ShoppingCartSerializer(serializers.ModelSerializer):

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'
