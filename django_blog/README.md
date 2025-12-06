Documentation
Authentication Flow:

Registration Process:

User fills registration form
Form validates email uniqueness and password strength
User account created with hashed password
User automatically logged in
Redirected to profile page


Login Process:

User enters credentials
Django authenticates against hashed password
Session created on success
Redirected to profile or requested page


Profile Management:

Only accessible to authenticated users
Users can update: username, email, first/last name
Email uniqueness validated
Changes saved to database


Logout Process:

Session destroyed
User redirected to login page
Confirmation message displayed



Security Features:

CSRF protection on all forms
Password hashing using Django's PBKDF2
Login required decorator for protected views
Session-based authentication
Form validation and error handling