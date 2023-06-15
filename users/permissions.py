from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
    
class IsUserAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
         request.user.is_authenticated
        )
    
class IsEmployeeOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view,obj:User):
        return  request.user.is_employee or obj == request.user 
        
        