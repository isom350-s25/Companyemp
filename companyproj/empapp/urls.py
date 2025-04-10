from django.urls import path
from empapp import views


urlpatterns = [
    path('show/', views.show_employee, name='show_employee'),
    path('salary/', views.show_salary, name='show_salary'),
    path('patterson/', views.show_patterson, name='show_patterson'),
    path('born/', views.show_born_after_1990, name='show_born_after_1990'),

]