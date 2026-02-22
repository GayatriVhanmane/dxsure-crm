from django import forms
from .models import Client, Employee

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # ADDED: 'revenue' to the end of the fields list so it shows up on the page
        fields = ['first_name', 'last_name', 'email', 'phone', 'company_name', 'industry', 'status', 'revenue']
        
        # Adding Bootstrap classes to the form fields
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in fields
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' # This automatically picks up the new 'salary' field!
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            
            # FIXED: Updated 'hire_date' to 'hired_on' to match your models.py
            'hired_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            # ADDED: The widget for the new salary field
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }