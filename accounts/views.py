from django.shortcuts import render, redirect , get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import EmployeeProfile , Attendance
from .forms import EmployeeForm , EditEmployeeForm , AttendanceForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.

@login_required
def employee_profile(request):
    employee = EmployeeProfile.objects.get(user=request.user)

    return render(request, 'accounts/employee_profile.html', {
        'employee': employee
    })

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return redirect('employee_profile')
    return wrapper

@login_required
@admin_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            employee = form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'accounts/add_employee.html', {'form': form})

@login_required
@admin_required
def employee_list(request):
    employees = EmployeeProfile.objects.select_related('user', 'department', 'role')
    return render(request, 'accounts/employee_list.html', {'employees': employees})

@login_required
def edit_employee(request, emp_id):
    employee = get_object_or_404(EmployeeProfile, id=emp_id)

    if request.method == 'POST':
        form = EditEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')   # ✅ redirect works now
    else:
        form = EditEmployeeForm(instance=employee)

    return render(request, 'accounts/edit_employee.html', {
        'form': form,
        'employee': employee
    })


@login_required
@admin_required
def delete_employee(request, emp_id):
    employee = get_object_or_404(EmployeeProfile, id=emp_id)

    if request.method == 'POST':
        user = employee.user
        employee.delete()
        user.delete()
        return redirect('employee_list')

    return render(request, 'accounts/delete_employee.html', {
        'employee': employee
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('employee_list')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def mark_attendance(request):

    # Admin ko attendance mark karne nahi dena
    if request.user.is_superuser:
        return redirect('attendance_list')   # ya employee_list

    # Employee ke liye
    try:
        employee = EmployeeProfile.objects.get(user=request.user)
    except EmployeeProfile.DoesNotExist:
        return redirect('employee_profile')

    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=timezone.now().date()
    )

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('employee_profile')
    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'accounts/mark_attendance.html', {
        'form': form
    })

@login_required
@admin_required
def attendance_list(request):
    records = Attendance.objects.select_related('employee').order_by('-date')
    return render(request, 'accounts/attendance_list.html', {
        'records': records
    })

def home(request):
    return render(request, 'accounts/base.html')