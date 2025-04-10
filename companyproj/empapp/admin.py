from django.contrib import admin
from .models import Employee
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'title')
# Register your models here.
admin.site.register(Employee, EmpAdmin)