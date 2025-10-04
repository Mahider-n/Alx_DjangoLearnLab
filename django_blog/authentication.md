Contents (short):

What it does: Registration (username + email + password), login/logout (Django built-in views), profile editing (bio/avatar).

Files to look at:

blog/forms.py: UserRegisterForm, UserUpdateForm, ProfileUpdateForm

blog/views.py: register, profile

blog/models.py: Profile (OneToOne)

blog/urls.py: register, login, logout, profile

Templates: blog/templates/blog/\*.html

How to test:

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Register at /register/, log in at /login/, edit at /profile/.

Deployment notes:

Configure media (serve via cloud storage or via proper server when DEBUG=False).

Enforce HTTPS, secure cookies, set CSRF_TRUSTED_ORIGINS if needed.

To add: email verification, password reset (Django has PasswordResetView etc.), social auth (django-allauth)
