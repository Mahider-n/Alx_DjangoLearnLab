
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import login_required

# --- Function-based view ---
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})
# --- Class-based view ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("home")  # redirect to home page (adjust as needed)
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# LoginView & LogoutView can be used directly in urls.py
class LoginView(LoginView):
    template_name = "relationship_app/login.html"

class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
def list_books(request):
    books = Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books":books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Admin View ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# --- Librarian View ---
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# --- Member View ---
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")