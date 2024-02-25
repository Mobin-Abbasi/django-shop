from django.db import models
from shop.models import Product


# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    address = models.CharField(max_length=250, verbose_name='ادرس')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی')
    province = models.CharField(max_length=50, verbose_name='محل سکونت')
    city = models.CharField(max_length=50, verbose_name='شهر')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]

    def __str__(self):
        return f'order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_post_cost(self):
        weight = sum(item.get_weight() for item in self.items.all())
        if weight < 1000:
            return 20000
        elif 1000 <= weight <= 2000:
            return 30000
        else:
            return 50000

    def get_final_cost(self):
        price = self.get_total_cost() + self.get_post_cost()
        return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_weight(self):
        return self.weight
