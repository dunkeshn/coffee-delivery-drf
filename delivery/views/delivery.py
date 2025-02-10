from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from common.views.mixins import ListViewSet, CRUDViewSet
from delivery.filters import ProductCategoryFilter, OrderFilter, CafeFilter, DeliveryFilter
from delivery.models.cafe import Cafe
from delivery.models.delivery import Delivery
from delivery.models.order import Order
from delivery.models.product import Product
from delivery.serializers.delivery import ProductSearchListSerializer, ProductRetrieveSerializer, \
    ProductCreateSerializer, ProductUpdateSerializer, ProductDeleteSerializer, ProductListSerializer, \
    OrderSearchListSerializer, OrderListSerializer, OrderRetrieveSerializer, OrderCreateSerializer, \
    OrderUpdateSerializer, OrderDeleteSerializer, DeliverySearchListSerializer, DeliveryListSerializer, \
    DeliveryRetrieveSerializer, DeliveryCreateSerializer, DeliveryUpdateSerializer, DeliveryDeleteSerializer, \
    CafeSearchListSerializer, CafeListSerializer, CafeRetrieveSerializer, CafeCreateSerializer, CafeUpdateSerializer, \
    CafeDeleteSerializer


# Товары
@extend_schema_view(
    list=extend_schema(
        summary='Поиск товаров',
        tags=['Товары'],
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Поиск по `id`"
            ),
            OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             description="Поиск по `названию` и `описанию`"),
            OpenApiParameter(name="category", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             enum=[choice[0] for choice in Product.Category.choices],
                             description="Фильтр по `категории`"),
            OpenApiParameter(name="ordering", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             enum=["price", '-price' "rating", '-rating'],
                             description="Сортировка: `price` (по возрастанию), `-price` (по убыванию), `rating`, `-rating`"),
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество страниц для пагинации"),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество элементов на одну страницу")
        ],
    )
)
class ProductSearchView(ListViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSearchListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductCategoryFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'rating']


@extend_schema_view(
    list=extend_schema(summary='Список всех товаров', tags=['Товары']),
    retrieve=extend_schema(summary='Товар детально', tags=['Товары']),
    create=extend_schema(summary='Создать товар', tags=['Товары']),
    update=extend_schema(summary='Изменить товар', tags=['Товары']),
    partial_update=extend_schema(summary='Изменить товар частично', tags=['Товары']),
    destroy=extend_schema(summary='Удалить товар', tags=['Товары']),
)
class ProductView(CRUDViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        elif self.action == 'update':
            return ProductUpdateSerializer
        elif self.action == 'partial_update':
            return ProductUpdateSerializer
        elif self.action == 'destroy':
            return ProductDeleteSerializer
        return self.serializer_class


# Заказы
@extend_schema_view(
    list=extend_schema(
        summary="Поиск заказов",
        tags=["Заказы"],
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Поиск по `id`"
            ),
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Поиск по `имени пользователя` и `адресу кофейни`"
            ),
            OpenApiParameter(
                name="delivery_status",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=[choice[0] for choice in Order.DeliveryStatus.choices],
                description="Фильтр по `статусу доставки`"
            ),
            OpenApiParameter(
                name="payment_method",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=[choice[0] for choice in Order.PaymentMethod.choices],
                description="Фильтр по методу оплаты"
            ),
            OpenApiParameter(
                name="ordering",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=["sum", "-sum", "waiting_time", "-waiting_time", "created_at", "-created_at"],
                description="Сортировка: `sum` (по возрастанию), `-sum` (по убыванию), `waiting_time`, "
                            "`-waiting_time`, `created_at`, `-created_at`"),
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество страниц для пагинации"),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество элементов на одну страницу")
        ],

    ),
)
class OrderSearchView(ListViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSearchListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['id', 'user__username', 'cafe__address']
    ordering_fields = ['sum', 'waiting_time', 'created_at']


@extend_schema_view(
    list=extend_schema(summary="Список всех заказов", tags=["Заказы"]),
    retrieve=extend_schema(summary="Детали заказа", tags=["Заказы"]),
    create=extend_schema(summary="Создать заказ", tags=["Заказы"]),
    update=extend_schema(summary="Изменить заказ", tags=["Заказы"]),
    partial_update=extend_schema(summary="Частично изменить заказ", tags=["Заказы"]),
    destroy=extend_schema(summary="Удалить заказ", tags=["Заказы"]),
)
class OrderView(CRUDViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderRetrieveSerializer
        elif self.action == 'create':
            return OrderCreateSerializer
        elif self.action == 'update':
            return OrderUpdateSerializer
        elif self.action == 'partial_update':
            return OrderUpdateSerializer
        elif self.action == 'destroy':
            return OrderDeleteSerializer
        return self.serializer_class


# Доставка

@extend_schema(
    summary="Поиск доставок",
    tags=["Доставки"],
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Поиск по `id`"
        ),
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Поиск по `имени пользователя` и `курьеру`"
        ),
        OpenApiParameter(
            name="ordering",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            enum=["time_left", "-time_left"],
            description="Сортировка: `time_left` (по возрастанию), `-time_left` (по убыванию)"),
        OpenApiParameter(
            name="page",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Количество страниц для пагинации"),
        OpenApiParameter(
            name="page_size",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Количество элементов на одну страницу")
    ],
)
class DeliverySearchView(ListViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySearchListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DeliveryFilter
    search_fields = ['user__username', 'courier__username']
    ordering_fields = ['time_left']


@extend_schema_view(
    list=extend_schema(summary="Список всех доставок", tags=["Доставки"]),
    retrieve=extend_schema(summary="Детали доставки", tags=["Доставки"]),
    create=extend_schema(summary="Создать доставку", tags=["Доставки"]),
    update=extend_schema(summary="Изменить доставку", tags=["Доставки"]),
    partial_update=extend_schema(summary="Частично изменить доставку", tags=["Доставки"]),
    destroy=extend_schema(summary="Удалить доставку", tags=["Доставки"]),
)
class DeliveryView(CRUDViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DeliveryRetrieveSerializer
        elif self.action == 'create':
            return DeliveryCreateSerializer
        elif self.action == 'update':
            return DeliveryUpdateSerializer
        elif self.action == 'partial_update':
            return DeliveryUpdateSerializer
        elif self.action == 'destroy':
            return DeliveryDeleteSerializer
        return self.serializer_class


@extend_schema(
    summary="Поиск кофеен",
    tags=["Кофейни"],
    parameters=[
        OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                         description="Поиск по `адресу`"),
        OpenApiParameter(name="barista_number", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY,
                         description="Поиск по `числу бариста`"),
        OpenApiParameter(name="id", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY,
                         description="Поиск по `id`"),
        OpenApiParameter(
            name="page",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Количество страниц для пагинации"),
        OpenApiParameter(
            name="page_size",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Количество элементов на одну страницу")
    ],
)
class CafeSearchView(ListViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSearchListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CafeFilter
    search_fields = ['address']


@extend_schema_view(
    list=extend_schema(summary="Список всех кофеен", tags=["Кофейни"]),
    retrieve=extend_schema(summary="Детали кофейни", tags=["Кофейни"]),
    create=extend_schema(summary="Создать кофейню", tags=["Кофейни"]),
    update=extend_schema(summary="Изменить кофейню", tags=["Кофейни"]),
    partial_update=extend_schema(summary="Частично изменить кофейню", tags=["Кофейни"]),
    destroy=extend_schema(summary="Удалить кофейню", tags=["Кофейни"]),
)
class CafeView(CRUDViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CafeRetrieveSerializer
        elif self.action == 'create':
            return CafeCreateSerializer
        elif self.action == 'update':
            return CafeUpdateSerializer
        elif self.action == 'partial_update':
            return CafeUpdateSerializer
        elif self.action == 'destroy':
            return CafeDeleteSerializer
        return self.serializer_class
