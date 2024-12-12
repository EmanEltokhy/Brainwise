from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, department_choices

router = DefaultRouter()
router.register('users', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('department_choices/', department_choices, name='department_choices'),
]
