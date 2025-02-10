from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from delivery.models.cart import Cart
from users.managers import CustomUserManager
from users.models.profile import Profile


class User(AbstractUser):
    username = models.CharField(
        'Никнейм', max_length=150, unique=True, null=True, blank=True
    )
    email = models.EmailField('Почта', max_length=64, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='pictures',
                                null=True,
                                blank=True,
                                verbose_name='Фото')
    subscriptions = models.ManyToManyField('self', blank=True, verbose_name='Подписки', symmetrical=False, related_name='subscription')
    subscribers = models.ManyToManyField('self', blank=True, verbose_name='Подписчики', symmetrical=False, related_name='subscriber')
    is_courier = models.BooleanField('Курьер', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username}'


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
        if not hasattr(instance, 'cart'):
            cart = Cart.objects.create(user=instance)
            cart.sum = Decimal('0.00')
            cart.save()

