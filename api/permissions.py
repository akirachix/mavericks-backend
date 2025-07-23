from rest_framework import permissions
from authentication.models import AppUser 

class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated and \
               hasattr(request.user, 'appuser_profile') and \
               request.user.appuser_profile.user_type == 'Seller'

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_staff:
            return True
        if request.user.is_authenticated and \
           hasattr(request.user, 'appuser_profile'):
            app_user_profile = request.user.appuser_profile

            if app_user_profile.user_type == 'Seller' and app_user_profile == obj.user:
                return True

        return False 

