from django.urls import path, include
from rest_framework.routers import DefaultRouter


from rest_framework.routers import DefaultRouter
from .views import (OfferViewSet, DiscountViewSet)


router = DefaultRouter()
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'discounts', DiscountViewSet, basename='discount')


urlpatterns = router.urls