from django.contrib import admin
from .models import EmployeeProfile, Department, Role ,Attendance

# Register your models here.

admin.site.register(EmployeeProfile)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Attendance)