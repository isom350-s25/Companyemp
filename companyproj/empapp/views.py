from django.shortcuts import render
from .models import Employee
from decimal import Decimal
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