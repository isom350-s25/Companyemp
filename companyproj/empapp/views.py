from django.shortcuts import render
from .models import Employee
from decimal import Decimal
from datetime import date
# Create your views here.
def index(request):
    employees = Employee.objects.all()
    context = {
        "employees" :employees
    }
    return render(request,"index.html",context)
def salary(request):
    salary = Employee.objects.filter(salary__gte = Decimal("1000.00"))
    context ={
        "salaries":salary
    }
    return render(request,"salary.html",context)
def name(request):
    name = Employee.objects.filter(name__icontains= "Patterson")
    context = {
        "names":name
    }
    return render(request,"name.html",context)
def born(request):
    born = Employee.objects.filter(DOB__lt = "1990-01-01")
    context = {
        "born":born
    }
    return render(request,"born.html",context)
def duration(request):
    duration = Employee.objects.all()
    for e in duration:
        if e.hire_date:
            e.hire_duration = (date.today() - e.hire_date).days
    total_salary = sum([e.salary for e in duration])
    average_salary = total_salary / len(duration) if duration else 0
    context = {
        "average_salary": average_salary,
        "duration": duration,

    }
   
    return render(request, "bonus.html", context)