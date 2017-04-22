from rest_framework.permissions import BasePermission
from .models import Transactions

class IsOwner(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Transactions):
            return obj.Owner == request.user
        return obj.Owner == request.user