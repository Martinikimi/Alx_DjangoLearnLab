from django.contrib import admin
from .models import Book

# Create a custom ModelAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in admin
    search_fields = ('title', 'author')                     # Enable search by title or author
    list_filter = ('publication_year',)                     # Enable filtering by year

# Register the model with the custom ModelAdmin
admin.site.register(Book, BookAdmin)

