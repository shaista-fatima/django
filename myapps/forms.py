from django import forms
from myapps.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        field="__all__"