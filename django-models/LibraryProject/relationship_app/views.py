from django.shortcuts import render
from .models import Book

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
  
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),                  # function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # include app urls
]


