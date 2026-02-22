from django.contrib import admin
from .models import Employee, Client

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'is_active')
    search_fields = ('last_name', 'employee_id')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'first_name', 'last_name', 'status')
    list_filter = ('status', 'industry')