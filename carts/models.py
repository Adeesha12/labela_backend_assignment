from django.utils import timezone
from django.conf import settings
from django.db import models
from products.models import Product

User = settings.AUTH_USER_MODEL


class ShoppingCart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
