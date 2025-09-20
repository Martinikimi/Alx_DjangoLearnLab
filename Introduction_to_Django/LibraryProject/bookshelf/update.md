### **3️⃣ update.md**

```markdown
# Update a Book

```python
from bookshelf.models import Book

# Update the title of "1984" to "Nineteen Eighty-Four"
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.get(id=book.id)