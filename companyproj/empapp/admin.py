from django.contrib import admin
from .models import Employee  # Import your Employee model

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'salary')  # Fields to display in the admin list view

# Register the Employee model with the customized admin
admin.site.register(Employee, EmployeeAdmin)