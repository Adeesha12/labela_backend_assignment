from django.urls import path
from .views import CartItemCreateView, ShoppingCartListCreateView

urlpatterns = [

    path('shopping-carts/', ShoppingCartListCreateView.as_view(),
         name='shopping-cart-item-list'),

    path('shopping-carts/<int:cart_id>/add-item/',
         CartItemCreateView.as_view(),
         name='add-cart-item'),
]
