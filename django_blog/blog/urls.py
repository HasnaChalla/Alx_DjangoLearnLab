from django.urls import path
from django.contrib.auth import views as auth_views  # Importing built-in views
from . import views
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, CommentCreateView,
                    CommentDeleteView, CommentUpdateView, TagPostListView, search)

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('search/', search, name='search'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<str:tag_name>/', TagPostListView.as_view(), name='tag-posts'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]