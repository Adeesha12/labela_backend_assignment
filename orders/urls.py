from django.urls import path
from .views import DeliveryCreateView, OrderItemCreateView, OrderListCreateView

urlpatterns = [

    path('orders/', OrderListCreateView.as_view(),
         name='order-list-create'),

    path('order-items/create/', OrderItemCreateView.as_view(),
         name='create-order-item'),

    path('deliveries/create/', DeliveryCreateView.as_view(),
         name='create-delivery'),

]
