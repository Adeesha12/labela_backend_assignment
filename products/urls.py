from django.urls import path
from .views import ProductListCreatView, ProductDeailsView

urlpatterns = [

    path('products/', ProductListCreatView.as_view(),
         name='product-list-create'),

    path('products/<int:pk>/', ProductDeailsView.as_view(),
         name='product-details'),

]
