from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import auth
from .forms import UserCreateForm
from .models import Category, Product


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request,
                  'all_product.html',
                  {'categories': categories,
                   'products': products})


def main(request):
    categories = Category.objects.all()

    products_hot=(Product.objects.all().order_by('-buy')[:4])

    products_new = Product.objects.all().order_by('-created')[:4]

    products_little = Product.objects.all().order_by('stock')[:4]
    user_form = UserCreateForm()
    return render(request, 'main.html', {'cat':categories,
                                         'hot_price':products_hot,
                                         'new_price':products_new,
                                         'little_price':products_little,
                                         'username': auth.get_user(request).username,
                                         'form':user_form})


def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})
