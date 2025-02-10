from django.urls import path, include
from rest_framework.routers import DefaultRouter

from delivery.views.delivery import ProductSearchView, ProductView, OrderView, OrderSearchView, DeliverySearchView, \
    DeliveryView, CafeSearchView, CafeView

router = DefaultRouter()

router.register(r'product/search', ProductSearchView, 'product_search')
router.register(r'product/manage', ProductView, 'product_manage')
router.register(r'order/search', OrderSearchView, 'order_search')
router.register(r'order/manage', OrderView, 'order_manage')
router.register(r'delivery/search', DeliverySearchView, 'delivery_search')
router.register(r'delivery/manage', DeliveryView, 'delivery_manage')
router.register(r'cafe/search', CafeSearchView, 'cafe_search')
router.register(r'cafe/manage', CafeView, 'cafe_manage')




urlpatterns = [

]

urlpatterns += path('delivery/', include(router.urls)),