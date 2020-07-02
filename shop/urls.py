from . import views
from django.views.generic import ListView

from .models import Product, Category

from django.urls import path

urlpatterns = [
    path('',views.main),
    path('product-detail/<slug:slug>',views.product_details,name='detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('filter/<slug:slug>/',views.filter,name='filter')
]
