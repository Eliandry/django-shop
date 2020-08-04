from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import auth
from django.views.generic import ListView

from .forms import UserCreateForm
from .models import Category, Product, Reviews
from cart.forms import CartAddProductForm


def main(request):
    categories = Category.objects.all()

    products_hot = (Product.objects.all().order_by('-buy')[:4])

    products_new = Product.objects.all().order_by('-created')[:4]

    products_little = Product.objects.all().order_by('stock')[:4]
    user_form = UserCreateForm()
    return render(request, 'main.html', {'cat': categories,
                                         'hot_price': products_hot,
                                         'new_price': products_new,
                                         'little_price': products_little,
                                         'username': auth.get_user(request).username,
                                         'form': user_form})


def product_details(request, id):
    product = get_object_or_404(Product,
                                id=id, )
    cart_product_form = CartAddProductForm()
    return render(request, 'detail.html', {'product': product,
                                           'cart_product_form': cart_product_form,
                                           'username': auth.get_user(request).username, })


class SearchView(ListView):
    template_name = 'filter.html'

    def get_queryset(self):
        name = self.request.GET.get('q')
        return Product.objects.filter(name=name.capitalize())


class AddReview(View):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        text = request.POST.get('textcomm')
        name = auth.get_user(request).first_name
        lastname = auth.get_user(request).last_name
        parent = None
        if request.POST.get('parent', None):
            parent = int(request.POST.get('parent'))
        review = Reviews(name=name, lastname=lastname, text=text, product=product, parent_id=parent)
        review.save()
        return HttpResponseRedirect(product.get_absolute_url())


def filter(request, slug):
    products = Product.objects.filter(category__slug=slug)
    category = Category.objects.get(slug=slug)
    return render(request, 'filter.html', {'product_list': products,
                                           'category': category})
