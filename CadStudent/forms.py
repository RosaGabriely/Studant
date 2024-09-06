# CadStudent/forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'cpf', 'birth_date', 'course_period', 'courses', 'photo']

