from django.shortcuts import render
from .models import Employee

# Create your views here.
def show_employee(request):
    employees = Employee.objects.all()
  
    return render(request, 'show_employee.html', {'employee': employees})

def show_salary(request):
    salary = Employee.objects.filter(salary__gt=1000)
    return render(request, 'salary.html', {'salar': salary})

def show_patterson(request):
    patterson = Employee.objects.filter(name__contains='Patterson')
    return render(request, 'patterson.html', {'patterso': patterson})

def show_born_after_1990(request):
    born_after_1990 = Employee.objects.filter(DOB__year__gt=1990)
    return render(request, '1990.html', {'born': born_after_1990})