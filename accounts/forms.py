from django import forms
from django.contrib.auth.models import User
from .models import EmployeeProfile , Attendance

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = EmployeeProfile
        fields = ['department', 'role', 'mobile']

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['department', 'role', 'mobile']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']