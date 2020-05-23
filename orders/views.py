from django.contrib import auth
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart=Cart(request)
    if request.method == 'POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.first_name=auth.get_user(request).first_name
            order.last_name = auth.get_user(request).last_name
            order.email = auth.get_user(request).username
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'created.html',
                          {'order': order})
    else:
        form=OrderCreateForm
    return render(request,'create.html',{'cart': cart, 'form': form})