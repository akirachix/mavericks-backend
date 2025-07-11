
from django.urls import path
from .views import OrderViewSet, OrderItemViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderitems', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]


