from rest_framework import serializers

from delivery.models.order import Order
from delivery.models.product import Product
from users.models.users import User


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
        )


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'availability',
            'image',
            'rating',
        )


class OrderShortSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'products',
        )
