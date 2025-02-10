import django_filters

from delivery.models.cafe import Cafe
from delivery.models.delivery import Delivery
from delivery.models.order import Order
from delivery.models.product import Product


class ProductCategoryFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Product.Category.choices)
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")

    class Meta:
        model = Product
        fields = ['id', 'category']


class OrderFilter(django_filters.FilterSet):
    delivery_status = django_filters.ChoiceFilter(choices=Order.DeliveryStatus.choices)
    payment_method = django_filters.ChoiceFilter(choices=Order.PaymentMethod.choices)
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")

    class Meta:
        model = Order
        fields = ['id', 'delivery_status', 'payment_method']


class DeliveryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")

    class Meta:
        model = Delivery
        fields = ['id']


class CafeFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")
    barista_number = django_filters.NumberFilter(field_name="barista_number", lookup_expr="exact")

    class Meta:
        model = Cafe
        fields = ['id', 'barista_number']
