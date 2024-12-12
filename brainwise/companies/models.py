from django.db import models
from django.db.models.deletion import ProtectedError


class Company(models.Model):
    name = models.CharField(max_length=200)
    number_of_departments = models.PositiveIntegerField(default=0, editable=False)
    number_of_employees = models.PositiveIntegerField(default=0, editable=False)

    def update_counts(self):
        self.number_of_departments = self.department_set.count()
        self.number_of_employees = self.employee_set.count()
        self.save()

    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
            if self.employee_set.exists() or self.department_set.exists():
                raise ProtectedError("Cannot delete company with employees or departments.", self)
            super().delete(*args, **kwargs)