# Organization Management System (OMS)

A **role-based Organization Management System** built using **Django (Python)** that allows admins to manage employees and attendance, while employees can securely access their profile and mark daily attendance.

This project follows **real-world architecture**, clean code practices, and proper **access control**.

![OMS Screenshot](static/emp_list.png)
![OMS Screenshot](static/attendance_list.png)

---

## Features

### Admin (Superuser)
- Login / Logout
![OMS Screenshot](static/login.png)
- Manage Employees (CRUD)
  - Add Employee
    ![OMS Screenshot](static/add_emp.png)
  - Edit Employee
  ![OMS Screenshot](static/edit_emp.png)
  - Delete Employee
 ![OMS Screenshot](static/del_confirm.png)
- View All Employees
- View Attendance of All Employees
- Secure admin-only access

### Employee (Normal User)
- Login / Logout
- View Own Profile
![OMS Screenshot](static/profile.png)
- Mark Daily Attendance (Present / Absent / Leave)
 ![OMS Screenshot](static/attendance.png)
- Cannot access admin pages
- No “Access Denied” errors (Smart Redirect UX)


---

## Tech Stack

- **Backend:** Django 5.1.3 (Python)
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (default)
- **Authentication:** Django Auth System

---

## 📁 Project Structure

organization_ms/
│
├── accounts/
│ ├── migrations/
│ ├── templates/
│ │ └── accounts/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── employee_list.html
│ │ ├── add_employee.html
│ │ ├── edit_employee.html
│ │ ├── delete_employee.html
│ │ ├── employee_profile.html
│ │ ├── attendance_list.html
│ │ └── mark_attendance.html
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── urls.py
│
├── organization_ms/
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md
---

## Database Models

### EmployeeProfile
- user (OneToOneField → Django User)
- department
- role
- mobile

### Attendance
- employee (ForeignKey)
- date
- status (Present / Absent / Leave)

---

## Authentication & Authorization

- Django built-in authentication
- Custom `admin_required` decorator
- Smart redirect instead of 403 errors
- Secure role-based page access

---

## Smart UX Flow

### Employee Login
**Login → Employee Profile → Mark Attendance → Logout**

### Admin Login
**Login → Admin Dashboard → Manage Employees / View Attendance → Logout**


