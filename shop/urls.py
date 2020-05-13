from . import views
from django.views.generic import ListView

from .models import Product, Category

from django.urls import path

urlpatterns = [
    path('',views.main),
    path('product-list/',views.product_list),
    path('product-detail/<int:id>',views.product_details),
]
