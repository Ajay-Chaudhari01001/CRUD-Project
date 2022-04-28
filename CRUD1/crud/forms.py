from django.core import validators
from tkinter import Widget
from django import forms
from .models import StudentData

# creating Form
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentData
        # ['name', 'email', 'branch', 'password']
        fields = "__all__" 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'branch': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            
        }
        