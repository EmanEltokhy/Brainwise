from rest_framework.viewsets import ModelViewSet
from .models import Employee, Department
from .serializers import EmployeeSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrManagerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManagerOrReadOnly]

    # def get_queryset(self):
    #     """
    #     Return employees filtered by company, department, or all employees by default.
    #     """
    #     queryset = super().get_queryset()
    #     if self.request.user.role == 'employee':
    #         return queryset
    #     company = self.request.query_params.get('company')  # Get 'company' from query parameters
    #     department = self.request.query_params.get('department')  # Get 'department' from query parameters
    #     print('company', company)
    #     print('department', department)

    #     if company:
    #         # Filter by company if 'company' parameter is provided
    #         queryset = queryset.filter(company_id=company)
    #     if department:
    #         # Filter by department if 'department' parameter is provided
    #         queryset = queryset.filter(department_id=department)

    #     return queryset
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def byId(self, request):
        """
        Endpoint to get data of the currently logged-in user.
        """
        departmentId = request.GET.get('id')
        print(departmentId)
        print("eman")
        queryset = Employee.objects.filter(department=departmentId)
        # print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        # serializer = DepartmentSerializer(queryset)
        return Response(serializer.data)

def department_choices(request):
    company_id = request.GET.get('company_id')
    if company_id:
        departments = Department.objects.filter(company_id=company_id).values('id', 'name')
        return JsonResponse({'departments': list(departments)})
    return JsonResponse({'departments': []})

# def change_employee_stage(request, employee_id):
#     employee = get_object_or_404(Employee, id=employee_id)
#     new_stage = request.GET.get('new_stage')

#     if new_stage not in Employee.STAGE_CHOICES:
#         return JsonResponse({"error": "Invalid stage."}, status=400)

#     try:
#         employee.change_stage(new_stage)
#         return JsonResponse({"success": f"Employee {employee.name} moved to {new_stage}."})
#     except ValidationError as e:
#         return JsonResponse({"error": str(e)}, status=400)