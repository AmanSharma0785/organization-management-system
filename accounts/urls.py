from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('' ,views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('edit-employee/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('profile/', views.employee_profile, name='employee_profile'),
]