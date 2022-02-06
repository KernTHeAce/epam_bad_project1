from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import AddEmployeeForm, AddDepartmentForm, FindEmployeeForm, FilterEmployeeForm
from django.shortcuts import redirect

def empl_number():
    dep_items = models.Department.objects.all()
    empl_counts = []
    for dep_item in dep_items:
        empl_counts.append(models.Employee.objects.filter(department=dep_item).count())
    return empl_counts
    

def department(request):
    items = models.Department.objects.all()
    data = {
        'items': items,
        'count': items.count(),
        }
    return render(request, 'department.html', data)

def find(request):
    error = ''
    form = FindEmployeeForm()

    if request.method == 'POST':
        form = FindEmployeeForm(request.POST)
        
        if form.is_valid():
            form.save
            return redirect('employees')
        else:
            error = 'Form was incorrect'

    items = models.Employee.objects.all()
    data = {
        'form': form,
        'items': items,
        'count': items.count()
        }
    return render(request, 'find.html', data)

def filter(request):
    error = ''
    form = FilterEmployeeForm()

    if request.method == 'POST':
        form = FilterEmployeeForm(request.POST)
        
        if form.is_valid():
            form.save
            return redirect('employees')
        else:
            error = 'Form was incorrect'

    items = models.Employee.objects.all()
    data = {
        'form': form,
        'items': items,
        'count': items.count()
        }
    return render(request, 'filter.html', data)

def employee(request):
    items = models.Employee.objects.all()
    data = {
        'items': items,
        'count': items.count()
        }
    return render(request, 'employee.html', data)

def add_employee(request):
    error = ''
    form = AddEmployeeForm()
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            error = 'Form was incorrect'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_employee.html', data)


def add_department(request):
    error = ''
    form = AddDepartmentForm()
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
        else:
            error = 'Form was incorrect'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_department.html', data)
