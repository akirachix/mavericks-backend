from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    PaymentsViewset,
    ProductViewSet,
    UserViewSet,
    OrderViewSet,
    OrderItemViewSet,
    OfferViewSet,
    DiscountViewSet,
    ReviewViewSet,  
    RateTraderViewSet,  
    CartViewSet,  
    CartItemViewSet,
)


router = DefaultRouter()
router.register(r'Payments', paymentsViewset, basename='Payments')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderitems', OrderItemViewSet, basename='orderitems')
router.register(r'payments', OrderViewSet, basename='payments')
router.register(r'offers', OfferViewSet, basename='offers')
router.register(r'discounts', DiscountViewSet, basename='discounts')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'rate_traders', RateTraderViewSet, basename='rate_traders')
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart_items', CartItemViewSet, basename='cart_items')


urlpatterns=[
    path('', include(router.urls)),
]








