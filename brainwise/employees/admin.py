# employees/admin.py
from django.contrib import admin
from django import forms
from .models import Employee, Department



class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = [
        'name', 
        'designation', 
        'company', 
        'department', 
        'status', 
        'hired_on', 
        'days_employed'
    ]
    list_filter = ['status', 'company', 'department']
    search_fields = ['name', 'email', 'designation']
    readonly_fields = ['days_employed']

    # Add JavaScript to dynamically update department choices based on the selected company
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'employees/js/employee_admin.js',  # Path to your JS file within the static directory
        )

# # employees/admin.py
# from django.contrib import admin
# from django import forms
# from .models import Employee, Department



# class EmployeeAdminForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'

#     # Add a field to change the employee's stage
#     new_stage = forms.ChoiceField(choices=Employee.STAGE_CHOICES, required=True)

#     def save(self, commit=True):
#         employee = super().save(commit=False)
#         new_stage = self.cleaned_data['new_stage']
#         employee.change_stage(new_stage)
#         return employee

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     form = EmployeeAdminForm
#     list_display = [
#         'name', 
#         'designation', 
#         'company', 
#         'department', 
#         'stage', 
#         'hired_on', 
#         'days_employed'
#     ]
#     list_filter = ['stage', 'company', 'department']
#     search_fields = ['name', 'email', 'designation']
#     readonly_fields = ['days_employed']

#     # Add JavaScript to dynamically update department choices based on the selected company
#     class Media:
#         js = (
#             'https://code.jquery.com/jquery-3.6.0.min.js',
#             'employees/js/employee_admin.js',  # Path to your JS file within the static directory
#         )