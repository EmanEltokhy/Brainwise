from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'number_of_employees']
    list_filter = ['company']
    search_fields = ['name']
    readonly_fields = ['number_of_employees']
