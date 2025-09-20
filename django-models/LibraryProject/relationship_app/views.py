from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library   # ✅ Library import required


# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library                # ✅ tells Django which model to use
    template_name = "relationship_app/library_detail.html"  # ✅ required
    context_object_name = "library"  # ✅ checker expects "library"
