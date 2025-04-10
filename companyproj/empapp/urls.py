from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index , name = "index"),
    path("salary/",views.salary , name = "salary" ),
    path("name/",views.name , name = "name" ),
    path("born/",views.born , name = "born" ),
    path("bonus/",views.duration , name = "bonus" ),

]
