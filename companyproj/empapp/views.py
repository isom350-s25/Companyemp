from django.shortcuts import render
from .models import Employee
from django.db.models import Avg
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()  
    return render(request, 'employee_list.html', {'employees': employees})

def employees_with_high_salary(request):
    employees = Employee.objects.filter(salary__gt=1000) 
    return render(request, 'employee_list.html', {'employees': employees})


def employees_named_patterson(request):
    employees = Employee.objects.filter(name="Patterson") 
    return render(request, 'employee_list.html', {'employees': employees})

def employees_born_after_1990(request):
    employees = Employee.objects.filter(date_of_birth__year__gt=1990) 
    return render(request, 'employee_list.html', {'employees': employees})

def employee_list(request):
    employees = Employee.objects.all()
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg']  # Calculate average salary
    return render(request, 'employee_list.html', {'employees': employees, 'avg_salary': avg_salary})

