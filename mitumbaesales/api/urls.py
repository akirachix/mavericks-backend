
from django.urls import path
from .views import OrderListCreateAPIView, OrderItemListCreateAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order-items/', OrderItemListCreateAPIView.as_view(), name='orderitem-list-create'),]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]


