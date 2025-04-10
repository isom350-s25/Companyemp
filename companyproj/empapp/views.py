from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee_list.html', {'employees': employees})