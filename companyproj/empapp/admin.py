from django.contrib import admin
from .models import Employee

# Customizing the admin view for Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'salary')  # Use 'title' instead of 'position'

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)