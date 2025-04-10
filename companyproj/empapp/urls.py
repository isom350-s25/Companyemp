from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_info, name='employee_info'),  # Default route for empapp/
    path('employee-info/', views.employee_info, name='employee_info'),
]