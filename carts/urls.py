from django.urls import path
# from .views import CartItemCreateView, ShoppingCartListCreateView,
from .views import CartItemRetrieveUpdateDestroyView ,CartItemCreateView

urlpatterns = [

#     path('shopping-carts/', ShoppingCartListCreateView.as_view(),
#          name='shopping-cart-list-create'),

#     path('shopping-carts/<int:cart_id>/add-item/',
#          CartItemCreateView.as_view(),
#          name='add-cart-item'),
    path('carts/<int:cart_id>/add-item/', CartItemCreateView.as_view(), name='add-cart-item'),
    path('carts/<int:cart_id>/cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-detail'),
]

