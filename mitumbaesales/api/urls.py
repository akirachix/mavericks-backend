<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentTransferViewSet

router = DefaultRouter()
router.register(r'payments',PaymentViewSet, basename="payments")
router.register(r'paymentTransfer',PaymentTransferViewSet, basename="paymentTransfer")
urlpatterns=[
    path('', include(router.urls)),
]
=======
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.views import paymentsViewset
router = DefaultRouter()
router.register(r'Payments', paymentsViewset, basename='Payments')
urlpatterns=[
    path("", include(router.urls)),
]
>>>>>>> feature/boilerplate
