
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.views import paymentsViewset
router = DefaultRouter()
router.register(r'Payments', paymentsViewset, basename='Payments')
urlpatterns=[
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]


