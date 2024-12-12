# from django.db import models
# from django.forms import ValidationError
# from companies.models import Company
# from departments.models import Department
# from datetime import date
# from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator

# class Employee(models.Model):
#     STATUS_CHOICES = [
#         ('onboarding', 'Onboarding'),
#         ('active', 'Active'),
#         ('inactive', 'Inactive'),
#     ]
#     # STAGE_CHOICES = [
#     # ('application_received', 'Application Received'),
#     # ('interview_scheduled', 'Interview Scheduled'),
#     # ('hired', 'Hired'),
#     # ('not_accepted', 'Not Accepted'),
# # ]

#     # Define the status field to track onboarding stage
#     # stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='application_received')


#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     department = models.ForeignKey(
#         Department, on_delete=models.CASCADE, related_name='employees'
#     )
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='onboarding')
#     name = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     mobile_number = models.CharField(validators=[phone_regex], max_length=16)
#     address = models.TextField()
#     title = models.CharField(max_length=100, null=True)
#     position = models.CharField(max_length=100, null=True)
#     designation = models.CharField(max_length=200, editable=False) 
#     hired_on = models.DateField(null=True, blank=True)

#     def clean(self):
#         if not self.name or not self.email or not self.mobile_number:
#             raise ValidationError("Name, Email, and Mobile Number are required.")
#         elif self.department.company != self.company:
#             raise ValidationError("The department must belong to the selected company.")
        
#     @property
#     def days_employed(self):
#         if self.hired_on:
#             return (date.today() - self.hired_on).days
#         return None
    
#     def valid_transitions(self):
#         valid_transitions = {
#             'application_received': ['interview_scheduled', 'not_accepted'],
#             'interview_scheduled': ['hired', 'not_accepted'],
#         }
#         return valid_transitions.get(self.stage, [])

#     def change_stage(self, new_stage):
#         """Method to change the stage with validation."""
#         if new_stage not in self.valid_transitions():
#             raise ValidationError(f"Cannot transition from {self.stage} to {new_stage}.")
#         self.stage = new_stage
#         self.save()

#     def save(self, *args, **kwargs):
#         self.designation = f"{self.title} - {self.position}"
#         super().save(*args, **kwargs)
#         self.company.update_counts()
#         self.department.update_employee_count()

#     def __str__(self):
#         return f"{self.name} - {self.stage}"

from django.db import models
from django.forms import ValidationError
from companies.models import Company
from departments.models import Department
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Employee(models.Model):
    STATUS_CHOICES = [
        ('onboarding', 'Onboarding'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='onboarding')
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=16)
    address = models.TextField()
    title = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=200, editable=False) 
    hired_on = models.DateField(null=True, blank=True)

    def clean(self):
        if not self.name or not self.email or not self.mobile_number:
            raise ValidationError("Name, Email, and Mobile Number are required.")
        elif self.department.company != self.company:
            raise ValidationError("The department must belong to the selected company.")
        
    @property
    def days_employed(self):
        if self.hired_on:
            return (date.today() - self.hired_on).days
        return None

    def save(self, *args, **kwargs):
        self.designation = f"{self.title} - {self.position}"
        super().save(*args, **kwargs)
        self.company.update_counts()
        self.department.update_employee_count()

    def __str__(self):
        return f"{self.name} ({self.designation})"
