from django.urls import path
from .views import ProductListCreatView, ProductDetailsView

urlpatterns = [

    path('products/', ProductListCreatView.as_view(),
         name='product-list-create'),

    path('products/<int:pk>/', ProductDetailsView.as_view(),
         name='product-details'),

]
