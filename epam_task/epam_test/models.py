from django.db import models
from django.db.models.fields import AutoField

class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_birth = models.DateField('Date of birth')
    salary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


