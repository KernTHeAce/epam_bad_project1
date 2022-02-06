from django.forms import DateField, ModelForm, TextInput, DecimalField
from django.forms.widgets import DateInput
from .models import Department, Employee
from django import forms

class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'date_of_birth', 'salary']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form_input',
                'autocomplete': 'off',
            }),

            'department': forms.Select(attrs={
                'placeholder': 'Department',
                'class': 'form_input',
            },
            choices = Department.objects.all()
            ),

            'date_of_birth': DateInput(attrs={
                'placeholder': 'Date Of Birth',
                'type': 'date',
                'color': 'white',
                'class': 'form_input',
                'value': '2001-01-01',
                'autocomplete': 'off',
            }),

            'salary': DateInput(attrs={
                'placeholder': 'Salary',
                'type': 'number',
                'step': '.01',
                'class': 'form_input',
                'autocomplete': 'off',
            })
        }


class AddDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']

        widgets = {
            'department_name': TextInput(attrs={
                'placeholder': 'Name of Department',
                'class': 'form_input',
                'autocomplete': 'off',
            })

        }

class FilterEmployeeForm(forms.Form):
    from_field = forms.DateField(label='', widget=forms.TextInput(attrs={
        'class': 'form_input',
        'type': 'date',
        'value': '2001-01-01',
        'color': 'white',
        'autocomplete': 'off',
        }))

    to_field = forms.DateField(label='', widget=forms.TextInput(attrs={
        'class': 'form_input',
        'type': 'date',
        'value': '2001-01-01',
        'color': 'white',
        'autocomplete': 'off',
        }))

class FindEmployeeForm(forms.Form):
    date = forms.DateField(label='', widget=forms.TextInput(attrs={
        'class': 'form_input',
        'type': 'date',
        'value': '2001-01-01',
        'color': 'white',
        'autocomplete': 'off',
        }))
    