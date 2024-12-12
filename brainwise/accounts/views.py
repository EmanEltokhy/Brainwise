from rest_framework.viewsets import ModelViewSet
from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Count
from employees.models import Employee
from departments.models import Department
from companies.models import Company
from django.db.models import Avg



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
class UserAccountViewSet(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Endpoint to get data of the currently logged-in user.
        """
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class AnalyticsSummaryView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access the API

    def get(self, request):
        # Aggregating data for companies and employees
        number_of_companies = Company.objects.count()
        number_of_departments = Department.objects.count()
        number_of_employees = Employee.objects.count()

        # You can add more summary data here, like active/inactive employees
        active_employees = Employee.objects.filter(status="active").count()
        inactive_employees = Employee.objects.filter(status="inactive").count()
        onboarding_employees = Employee.objects.filter(status="onboarding").count()

        top_companies = Company.objects.annotate(employee_count=Count('employee')).order_by('-employee_count')[:3]
        top_companies_data = [
            {"name": company.name, "employee_count": company.employee_count} for company in top_companies
        ]

        # # Average employees per company
        avg_employees_per_company = Employee.objects.aggregate(average=Avg('company__employee'))['average']



        data = {
            "number_of_companies": number_of_companies,
            "number_of_departments": number_of_departments,
            "number_of_employees": number_of_employees,

            "active_employees": active_employees,
            "inactive_employees": inactive_employees,
            "onboarding_employees": onboarding_employees,
            "top_companies_data": top_companies_data,
            "avg_employees_per_company": avg_employees_per_company
        }

        return Response(data)
