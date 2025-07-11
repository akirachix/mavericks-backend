from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet

from .views import OfferViewSet, DiscountViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')
router.register(r'offers', OfferViewSet)
router.register(r'discounts', DiscountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


