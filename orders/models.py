from django.conf import settings
from django.db import models
from products.models import Product

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_date_time = models.DateTimeField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_date_time = models.DateTimeField()
