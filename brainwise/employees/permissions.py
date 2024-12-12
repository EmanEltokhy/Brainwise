from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrManagerOrReadOnly(BasePermission):
    """
    Custom permission to allow:
    - Admins and Managers: Full access (CRUD).
    - Employees: Read-only access to all employees.
    - Unauthenticated users: No access.
    """

    def has_permission(self, request, view):
        # Safe methods (GET, HEAD, OPTIONS) are allowed for all authenticated users
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Non-safe methods (POST, PUT, DELETE) are allowed only for admins or managers
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']
