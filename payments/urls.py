from django.urls import path
from .views import InitiateSTKPushView, mpesa_callback

urlpatterns = [
    path('initiate-stk-push/', InitiateSTKPushView.as_view(), name='initiate_stk_push'),
    path('mpesa-callback/', mpesa_callback, name='mpesa_callback'),
]

