from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','review')
        labels = {
            'fullname':'Full Name(Enter your full name please)',
            'review':'Reviews(Write your experience with us)',


        }
