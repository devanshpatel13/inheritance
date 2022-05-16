from django import forms
from .models import *


class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields='__all__'

class Teacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields ='__all__'