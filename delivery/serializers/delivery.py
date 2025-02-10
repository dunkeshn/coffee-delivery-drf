from rest_framework import serializers

from common.serializers.common import UserShortSerializer, ProductShortSerializer, OrderShortSerializer
from common.serializers.mixins import ExtendedModelSerializer
from delivery.models.cafe import Cafe
from delivery.models.delivery import Delivery
from delivery.models.order import Order
from delivery.models.product import Product


# Товары
class ProductSearchListSerializer(ExtendedModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    availability_display = serializers.CharField(source='get_availability_display', read_only=True)

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category_display',
                  'availability_display',
                  'image',
                  'rating')


class ProductListSerializer(ExtendedModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    availability_display = serializers.CharField(source='get_availability_display', read_only=True)

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category_display',
                  'availability_display',
                  'image')


class ProductRetrieveSerializer(ExtendedModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    availability_display = serializers.CharField(source='get_availability_display', read_only=True)

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category_display',
                  'availability_display',
                  'image')


class ProductCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category',
                  'availability',
                  'image')

class ProductUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category',
                  'availability',
                  'image')


class ProductDeleteSerializer(ExtendedModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    availability_display = serializers.CharField(source='get_availability_display', read_only=True)

    class Meta:
        model = Product
        fields = ('name',
                  'price',
                  'description',
                  'category_display',
                  'availability_display',
                  'image')


# Заказы

class OrderSearchListSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )


class OrderListSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )


class OrderRetrieveSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )


class OrderCreateSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )

    def create(self, validated_data):
        user = validated_data['user']
        cart = user.cart

        order = Order.objects.create(
            user=user,
            sum=cart.sum,
            delivery_status=Order.DeliveryStatus.PAYING
        )

        order.copy_from_cart()

        return order


class OrderUpdateSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )


class OrderDeleteSerializer(ExtendedModelSerializer):
    delivery_status_display = serializers.CharField(source='get_delivery_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    user = UserShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = ('sum',
                  'delivery_status_display',
                  'payment_method_display',
                  'address',
                  'waiting_time',
                  'user',
                  'products'
                  )


# Доставка

class DeliverySearchListSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()

    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')


class DeliveryListSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()
    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')


class DeliveryRetrieveSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()
    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')


class DeliveryCreateSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()
    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')

    def validate_courier(self,
                         value):
        if not value.is_courier:
            raise serializers.ValidationError("Только пользователь с ролью 'курьер' может быть назначен.")
        return value


class DeliveryUpdateSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()
    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')


class DeliveryDeleteSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    courier = UserShortSerializer()
    order = OrderShortSerializer()
    class Meta:
        model = Delivery
        fields = ('user',
                  'order',
                  'courier',
                  'latitude',
                  'longitude')


# Кофейни

class CafeSearchListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'


class CafeListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'


class CafeRetrieveSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'


class CafeCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'


class CafeUpdateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'


class CafeDeleteSerializer(ExtendedModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'
