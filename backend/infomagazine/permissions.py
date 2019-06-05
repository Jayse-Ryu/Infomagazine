from rest_framework.permissions import BasePermission

# class CommonPermission(BasePermission):
#     def __eval_access_role(self,role):
#         return None
from user.models import AccessRole


def _eval_access_role(request, role):
    if request.user.is_authenticated:
        return request.user.get_access_role() <= role
    else:
        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and _eval_access_role(request, AccessRole.OWNER))


class IsMarketer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and _eval_access_role(request, AccessRole.MARKETER))


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and _eval_access_role(request, AccessRole.CLIENT))
