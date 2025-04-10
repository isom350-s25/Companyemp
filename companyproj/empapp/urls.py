from django.urls import path
from .views import show_employees, employees_salary_above1000, employees_born_after1990, employees_avg_salary


urlpatterns = [
    path('employees/', show_employees, name='show_employees'),
    path('salary/', employees_salary_above1000, name='salary'),
    path('born/', employees_born_after1990, name='born'),
    path('avg/', employees_avg_salary, name='avg_salary'),
]