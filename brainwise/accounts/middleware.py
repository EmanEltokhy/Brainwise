from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

class RestrictEmployeeAdminAccessMiddleware:
    """
    Middleware to prevent users with 'employee' role from accessing the admin panel.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin panel
        if request.path.startswith('/admin/'):
            user = request.user
            if user.is_authenticated and hasattr(user, 'role') and user.role == 'employee':
                # Show forbidden message if first time accessing
                if not request.session.get('employee_forbidden_shown'):
                    request.session['employee_forbidden_shown'] = True
                    return HttpResponseForbidden("You do not have permission to access the admin panel.")
                else:
                    # Log the user out and redirect to admin login after forbidden message
                    logout(request)
                    request.session['employee_forbidden_shown'] = False
                    return HttpResponseRedirect(reverse('admin:login'))

        return self.get_response(request)
