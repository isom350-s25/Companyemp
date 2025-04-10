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
    employees = Employee.objects.filter(salary__gte = Decimal("1000.00"))
    context ={
        "employees":employees
    }
    return render(request,"index.html",context)