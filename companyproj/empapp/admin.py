from django.contrib import admin
from .models import Employee


# Register your models here.
#admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary')
    
    def name(self,obj):
        return obj.name
    name.short_description = 'Name'

    def position(self, obj):
        return obj.title
    position.short_description = 'Position'

    def salary(self,obj):
        return obj.salary
    salary.short_description = 'Salary'

admin.site.register(Employee, EmployeeAdmin)
   