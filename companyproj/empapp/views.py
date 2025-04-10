from django.shortcuts import render
from .models import Employee  
from datetime import date  
from django.db.models import Avg

# Create your views here.
def employee_info(request):
    employee_info = Employee.objects.all()

    for employee in employee_info:
        if employee.hire_date:  
            employee.hire_duration = (date.today() - employee.hire_date).days  

    employees_salary = Employee.objects.filter(salary__gt=1000)
    employees_name = Employee.objects.filter(name__startswith='Patterson')
    employees_born = Employee.objects.filter(DOB__year__gt=1990)  
    average_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg']

    context = {
        'employee_info': employee_info,
        'employees_salary': employees_salary,
        'employees_name': employees_name,
        'employees_born': employees_born,
        'average_salary': average_salary,
    }
    return render(request, 'employee.html', context)