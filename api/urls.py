from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppUserViewSet 
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    ProductViewSet,
    OrderViewSet,
    RegisterView,
    LoginView,
    LogoutView,
    OfferViewSet,
    DiscountViewSet,
    ReviewViewSet,  
    RateTraderViewSet,  
    CartViewSet,  
    CartItemViewSet,
    AppUserViewSet,

)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', AppUserViewSet, basename='user')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'offers', OfferViewSet, basename='offers')
router.register(r'discounts', DiscountViewSet, basename='discounts')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'rate_traders', RateTraderViewSet, basename='rate_traders')
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart_items', CartItemViewSet, basename='cart_items')
router.register(r'appusers', AppUserViewSet)


urlpatterns=[
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]




















