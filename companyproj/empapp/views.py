from django.shortcuts import render
from .models import Employee

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



