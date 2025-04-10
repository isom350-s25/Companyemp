from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('salary/', views.employee_sal, name='employee_sal'),
    path('pater/', views.employee_by_name, name='employee_by_name'),
    path('born/', views.employee_born_after_1990, name='employee_born_after_1990'),
]