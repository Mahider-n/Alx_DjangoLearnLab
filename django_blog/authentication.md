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

Access control: Only authenticated users can create posts; only the author can edit/delete.

Navigation: List → Detail → Create/Edit/Delete.

URLs: /posts/, /posts/new/, /posts/<pk>/, /posts/<pk>/edit/, /posts/<pk>/delete/.

Include this explanation in your README or as code comments.

Add Comment: /posts/<post_id>/comments/new/ → POST by authenticated users.

Edit Comment: /comments/<comment_id>/edit/ → Only author can edit.

Delete Comment: /comments/<comment_id>/delete/ → Only author can delete.

Permissions: Checked via login_required and filtering by author=request.user.