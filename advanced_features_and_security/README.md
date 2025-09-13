# LibraryProject

This is a basic Django project created for learning Django development environment setup.

## Steps to Run

1. Install Django: `pip install django`
2. Start the server: `python manage.py runserver`
3. Open `http://127.0.0.1:8000/` in a web browser to view the project.

## Project Structure

- **manage.py**: Command-line utility to manage the project.
- **LibraryProject/settings.py**: Configuration file for the project.
- **LibraryProject/urls.py**: URL mappings for the project.
- **LibraryProject/asgi.py & wsgi.py**: Entry points for ASGI/WSGI servers.

# The Book model has custom permissions: can_view, can_create, can_edit, can_delete

# Groups created: Editors (create/edit), Viewers (view only), Admins (all permissions)

# Use @permission_required decorator in views to enforce these permissions
