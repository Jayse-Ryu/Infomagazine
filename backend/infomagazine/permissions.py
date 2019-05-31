from rest_framework.permissions import BasePermission


def eval_access_role(request, role):
    return request.user.get_access_role() == role


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and eval_access_role(request, "OWNER"))


class IsMarketer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and eval_access_role(request, "Marketer"))


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and eval_access_role(request, "Client"))
