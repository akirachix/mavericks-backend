from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, RateTraderViewSet
from .views import CartViewSet, CartItemViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'rate-traders', RateTraderViewSet, basename='rate-trader')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')


# The API URLs are now determined automatically by the router.
urlpatterns = [
   path('', include(router.urls)),
]
