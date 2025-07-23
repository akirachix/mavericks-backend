from django.urls import path
from .views import OrderListCreateAPIView, OrderItemListCreateAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order-items/', OrderItemListCreateAPIView.as_view(), name='orderitem-list-create'),
]