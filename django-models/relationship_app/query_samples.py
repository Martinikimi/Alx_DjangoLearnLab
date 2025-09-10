import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

library = Library.objects.first()
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

librarian = library.librarian
print(f"Librarian for {library.name}: {librarian.name}")

