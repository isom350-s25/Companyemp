from django.shortcuts import render
from django.db.models import Avg
from .models import Employee
from datetime import date

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employee records
    return render(request, 'employee_list.html', {'employees': employees})

def employee_sal(request):
    employees = Employee.objects.filter(salary__gt=1000)  # Filter employees with salary > 1000
    return render(request, 'employee_list.html', {'employees': employees})

def employee_by_name(request):
    employees = Employee.objects.filter(name__icontains="Patterson")  # Filter employees with name "Patterson"
    return render(request, 'employee_list.html', {'employees': employees})

def employee_born_after_1990(request):
    employees = Employee.objects.filter(DOB__year__gt=1990)  # Filter employees born after 1990
    return render(request, 'employee_list.html', {'employees': employees})

def employee_hire_duration(request):
    employees = Employee.objects.all()
    for employee in employees:
        if employee.hire_date:  # Check if hire_date is not None
            employee.hire_duration = (date.today() - employee.hire_date).days
        else:
            employee.hire_duration = "N/A"  # Assign "N/A" if hire_date is None
    return render(request, 'employee_list.html', {'employees': employees, 'show_hire_duration': True})

def employee_average_salary(request):
    average_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg']  # Calculate average salary
    return render(request, 'employee_average_salary.html', {'average_salary': average_salary})



