from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.department, name='departments'),
    path('employee/', views.employee, name='employees'),
    path('employee/new/', views.add_employee),
    path('department/new/', views.add_department),
    path('employee/find/', views.find),
    path('employee/filter/', views.filter),
]