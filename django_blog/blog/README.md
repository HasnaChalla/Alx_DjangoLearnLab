# Django Blog Authentication System

A Django-based blog application with a comprehensive user authentication system featuring registration, login, logout, and profile management.

## 📋 Features

- **User Registration**: Sign up with username, email, and password
- **User Login**: Secure authentication with session management
- **User Logout**: Clean session termination
- **Profile Management**: View and edit user profile information
- **Security**: CSRF protection, password hashing, and authentication decorators
- **Responsive Design**: Mobile-friendly interface

## 🛠️ Technologies Used

- **Backend**: Django 5.1
- **Database**: SQLite3 (development) / PostgreSQL (production-ready)
- **Frontend**: HTML5, CSS3
- **Authentication**: Django's built-in authentication system

## 📁 Project Structure
```
django_blog/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── register.html
│   │       ├── login.html
│   │       └── profile.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
└── README.md
```