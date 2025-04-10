from django.shortcuts import render
from .models import Employee
import datetime
from django.db.models import Avg

# Create your views here.
def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def employees_salary_above1000(request):
    employees = Employee.objects.filter(salary__gt=1000)
    return render(request, 'employees.html', {'employees': employees})

def employees_born_after1990(request):
    date = datetime.date(1990, 1, 1)
    employees = Employee.objects.filter(DOB__gt=date)
    return render(request, 'employees.html', {'employees': employees})

def employees_avg_salary(request):
    avg_salary = Employee.objects.aggregate(Avg('salary'))
    return render(request, 'avg_salary.html', {'avg_salary': avg_salary})


def name_patterson(request):
    employees = Employee.objects.filter(name__icontains='patterson') 
    return render(request, 'employees.html', {'employees': employees})