from django.urls import path
from .views import employee_list
from .views import employees_with_high_salary
from .views import employees_named_patterson
from .views import employees_born_after_1990
urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/high-salary/', employees_with_high_salary, name='employees_with_high_salary'),
    path('employees/patterson/', employees_named_patterson, name='employees_named_patterson'),
    path('employees/born-after-1990/', employees_born_after_1990, name='employees_born_after_1990'),
]


from .views import employees_born_after_1990

