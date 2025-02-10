from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from common.models.mixins import DateMixin
from delivery.models.cafe import Cafe
from delivery.models.cart import Cart
from delivery.models.product import Product
from users.models.users import User


class Order(DateMixin):

    class DeliveryStatus(models.TextChoices):
        PAYING = 'PAYING', 'Оплата заказа'
        PREPARING = 'PREPARING', 'Заказ готовится'
        DELIVERING = 'DELIVERING', 'Заказ доставляется'
        RECEIVED = 'RECEIVED', 'Заказ получен'

    class PaymentMethod(models.TextChoices):
        BANK_CARD = 'BANK_CARD', 'Банковская карта'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='orders', verbose_name = 'Пользователь', null=True)
    products = models.ManyToManyField(to=Product, related_name='orders',
                                      verbose_name='Товары')
    cafe = models.ForeignKey(to=Cafe, on_delete=models.PROTECT, related_name='orders', verbose_name='Кофейни',
                             null=True)
    sum = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    delivery_status = models.CharField('Статус доставки', max_length=100, choices=DeliveryStatus.choices, default=DeliveryStatus.PAYING)
    payment_method = models.CharField('Способ оплаты', max_length=100, choices=PaymentMethod.choices, null=True, default=PaymentMethod.BANK_CARD)
    address = models.TextField('Адрес')
    waiting_time = models.TimeField('Ожидаемое время доставки', blank=True, default='00:05:00')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('waiting_time', )

    def __str__(self):
        return self.address

#     def copy_from_cart(self):
#         cart = self.user.cart
#         self.products.set(cart.products.all())  # Копируем все товары из корзины
#         self.sum = cart.sum  # Устанавливаем сумму из корзины
#         self.save()
#
# @receiver(post_save, sender=Cart)
# def create_order_from_cart(sender, instance, created, **kwargs):
#     if created:
#         # Создание нового заказа из корзины пользователя
#         order = Order.objects.create(user=instance.user, sum=instance.sum, delivery_status=Order.DeliveryStatus.PAYING)
#         order.copy_from_cart()  # Копируем данные из корзины в заказ