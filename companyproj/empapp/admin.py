from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'salary')
    