# oreilly-library


## Functional Requirements:

User should be able to find book metadata by supplying the author, ISBN, title, or description fields to a request.

User should be able to add book metadata.


## Non-Functional Requirements:

Book metadata must be stored in the database with the required fields ISBN, author, title, and description.

There should be no more than 200 books in the database.

The book metadata search query is a GET request should return json.

## Datamodels:

```python

class BookMetadata:
  def __init__(self, title, author, isbn, created_at=None description=""):
    self.description = description
    self.author = author
    self.isbn = isbn
    self.title = title
    self.created_at = datetime.datetime.now().isoformat() if not created_at else created_at

```
