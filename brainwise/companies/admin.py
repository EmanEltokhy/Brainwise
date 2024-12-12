from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_departments', 'number_of_employees']
    search_fields = ['name']
    readonly_fields = ['number_of_departments', 'number_of_employees']
