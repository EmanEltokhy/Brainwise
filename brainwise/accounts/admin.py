from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']
    list_filter = ['role']
    search_fields = ['username', 'email']
