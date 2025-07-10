from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.views import paymentsViewset
router = DefaultRouter()
router.register(r'Payments', paymentsViewset, basename='Payments')
urlpatterns=[
    path("", include(router.urls)),
]
