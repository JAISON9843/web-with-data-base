from django import forms
from dlm.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields={'sname','semail','course','fee'}
