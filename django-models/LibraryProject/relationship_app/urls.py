
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Authentication
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Existing book and library views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]

from django.urls import path
from .views import admin_dashboard

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    
    # Secured CRUD operations
    path('books/add/', views.add_book, name='add-book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit-book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete-book'),
]
