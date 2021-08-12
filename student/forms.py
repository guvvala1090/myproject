from django.forms import ModelForm
from .models import Student_Data
from django.contrib.auth.models import User
from django import forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_Data
        fields = '__all__'