from rest_framework import serializers
from .models import Order, OrderItem, Delivery
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'
