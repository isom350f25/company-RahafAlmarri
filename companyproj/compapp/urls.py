from django.urls import path
from . import views

urlpatterns = [
    path('employee_list/', views.employee_list, name = "employee_list"),
]