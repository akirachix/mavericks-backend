from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OfferViewSet, DiscountViewSet, OfferDiscountViewSet, OfferProductViewSet, NotificationViewSet
)

router = DefaultRouter()
router.register(r'offer', OfferViewSet, basename='offer')
router.register(r'discount', DiscountViewSet, basename='discount')
router.register(r'offerdiscount', OfferDiscountViewSet, basename='offerdiscount')
router.register(r'offerproduct', OfferProductViewSet, basename='offerproduct')
router.register(r'notification', NotificationViewSet, basename='notification')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('offer.urls')),   ]