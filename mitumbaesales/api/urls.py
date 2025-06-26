from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

from rest_framework.routers import DefaultRouter
from .views import (OfferViewSet, DiscountViewSet)
from .views import NotificationViewSet

router = DefaultRouter()
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'discounts', DiscountViewSet, basename='discount')
router.register(r'notifications', NotificationViewSet, basename='notification')


urlpatterns = router.urls