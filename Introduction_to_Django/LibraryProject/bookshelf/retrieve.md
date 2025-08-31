### **2️⃣ retrieve.md**

```markdown
# Retrieve a Book

```python
from bookshelf.models import Book


# Retrieve all books
books = Book.objects.get(title="1984")
for b in books:
    print(b.id, b.title, b.author, b.publication_year)
