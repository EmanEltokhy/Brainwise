# from rest_framework import serializers
# from .models import Employee

# class EmployeeSerializer(serializers.ModelSerializer):
#     days_employed = serializers.ReadOnlyField()

#     class Meta:
#         model = Employee
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Employee
# from departments.models import Department

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['company', 'department', 'status', 'name', 'email', 'mobile_number', 'address', 'designation', 'hired_on']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         company = self.initial_data.get('company')
#         if company:
#             self.fields['department'].queryset = Department.objects.filter(company_id=company)
#         elif self.instance:
#             self.fields['department'].queryset = self.instance.company.department_set.all()
from rest_framework import serializers
from .models import Employee
from departments.models import Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'company', 'department', 'status', 'name', 'email', 'mobile_number', 'address', 'designation', 'hired_on']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Deserialization process
        if hasattr(self, 'initial_data') and self.initial_data.get('company'):
            company = self.initial_data.get('company')
            self.fields['department'].queryset = Department.objects.filter(company_id=company)

        # Serialization process
        elif self.instance:
            if isinstance(self.instance, Employee):
                self.fields['department'].queryset = self.instance.company.department_set.all()
            elif hasattr(self.instance, '__iter__'):  # If queryset
                companies = {emp.company for emp in self.instance if emp.company}
                if len(companies) == 1:  # All employees belong to the same company
                    company = next(iter(companies))
                    self.fields['department'].queryset = company.department_set.all()
                else:
                    self.fields['department'].queryset = Department.objects.none()
