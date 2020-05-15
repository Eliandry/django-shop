from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    CHOICES = (
        ('Moscow', 'Москва'),
        ('Kyiv', 'Киев'),
        ('St.Petersburg', 'Санкт-Петербург'),
        ('Kazan', 'Казань')
    )
    user = models.ForeignKey(User, on_delete=True)
    city = models.CharField(choices=CHOICES, max_length=100, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый код')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=True)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity