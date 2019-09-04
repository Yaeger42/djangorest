from rest_framework.permissions import BasePermission
from .models import BucketList
'''This class implemetns a permission which holds by this truth - 
The user has to be the owner to have that objects permission. If they are indeed the owner of that bucketlist, it returns True, else False
'''
class IsOwner(BasePermission):
    """Base permission class to allow only bucketlist owners to edit them"""
    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted to the bucketlist owner"""
        if isinstance(obj, BucketList):
            return obj.owner == request.owner
        return obj.owner == request.user