from django.db import models
from companies.models import Company

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number_of_employees = models.PositiveIntegerField(default=0, editable=False)

    def update_employee_count(self):
        self.number_of_employees = self.employees.count()
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.company.update_counts()

    def __str__(self):
        return f"{self.name} ({self.company.name})"
