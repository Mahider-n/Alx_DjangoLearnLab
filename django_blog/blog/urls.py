from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post_list'),  # list view can stay plural
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # singular 'post/new/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # singular 'update'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # singular 'delete'
    
 
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
