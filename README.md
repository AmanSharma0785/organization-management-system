# Organization Management System (OMS)

A **role-based Organization Management System** built using **Django (Python)** that allows admins to manage employees and attendance, while employees can securely access their profile and mark daily attendance.

This project follows **real-world architecture**, clean code practices, and proper **access control**.

![OMS Screenshot](static/emp_list.png)
![OMS Screenshot](static/attendance_list.png)

---

## Features

### Admin (Superuser)
- **View All Employees**
- **View Attendance of All Employees**
- **Secure admin-only access**
- **Login / Logout**
  
    ![OMS Screenshot](static/login.png)
- **Manage Employees (CRUD)**
  - ***Add Employee***
    
    ![OMS Screenshot](static/add_emp.png)
  - ***Edit Employee***
    
  ![OMS Screenshot](static/edit_emp.png)
  - ***Delete Employee***
    
 ![OMS Screenshot](static/del_confirm.png)


### Employee (Normal User)
- **Login / Logout**
- **Cannot access admin pages**
- **No “Access Denied” errors (Smart Redirect UX)**
- **View Own Profile**
  
    ![OMS Screenshot](static/profile.png)
- **Mark Daily Attendance (Present / Absent / Leave)**
  
    ![OMS Screenshot](static/attendance.png)



---

## Tech Stack

- **Backend:** Django 5.1.3 (Python)
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (default)
- **Authentication:** Django Auth System

---

## 📁 Project Structure

<pre>
organization_ms/<br>
│<br>
├── accounts/<br>
│   ├── migrations/<br>
│   ├── templates/<br>
│   │   └── accounts/<br>
│   │       ├── base.html<br>
│   │       ├── login.html<br>
│   │       ├── employee_list.html<br>
│   │       ├── add_employee.html<br>
│   │       ├── edit_employee.html<br>
│   │       ├── delete_employee.html<br>
│   │       ├── employee_profile.html<br>
│   │       ├── attendance_list.html<br>
│   │       └── mark_attendance.html<br>
│   ├── models.py<br>
│   ├── views.py<br>
│   ├── forms.py<br>
│   └── urls.py<br>
│<br>
├── organization_ms/<br>
│   ├── settings.py<br>
│   └── urls.py<br>
│<br>
├── db.sqlite3<br>
├── manage.py<br>
└── README.md<br>
</pre>



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


