import pdb
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.db import models
from delivery.models.product import Product

# User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь', null=True)
    products = models.ManyToManyField(to=Product, related_name='carts', verbose_name='Товары', null=True, blank=True )
    sum = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('id', )

    def __str__(self):
        return f'Корзина #{self.id} - Сумма: {self.sum}'

    def calculate_sum(self):
        return sum(product.price for product in self.products.all())

@receiver(m2m_changed, sender=Cart.products.through)
def update_cart_sum(sender, instance, action, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        instance.sum = instance.calculate_sum()
        instance.save()