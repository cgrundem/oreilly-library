import services.books.book_metadata_repo as bmr



class BookMetadataService:
  def __init__(self, repository: bmr.BookMetadataRepository):
    self._repo: bmr.BookMetadataRepository = repository

  def find_books_by_search_query(self, query):
    return self._repo.find_books_by_search_query(query)