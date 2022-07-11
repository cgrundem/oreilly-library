import services.books.book_metadata_repo as bmr
from services.api.oreilly_api_client import OReillyAPIClient
from services.books.book_query_factory import BookQueryFactory



class BookMetadataService:
  def __init__(self, repository: bmr.BookMetadataRepository, query_factory: BookQueryFactory, api_client: OReillyAPIClient):
    self._repo: bmr.BookMetadataRepository = repository
    self._api_client: OReillyAPIClient = api_client
    self._query_factory: BookQueryFactory = query_factory

  def find_books_by_search_query(self, query):
    return self._repo.find_books_by_search_query(query)
  
  def extract_and_load_books(self, query):
    try:
      transformed_books = self._api_client.get_books_test(self._query_factory.make_oreilly_query_request_model(query))
      self.save_books(transformed_books)
      return transformed_books
    except Exception as e:
      return e
    
    
  def get_books(self, query):
    pass
  
  def get_all_books(self):
    return self._repo.get_all_books()
  
  def save_books(self, books_to_save):
    self._repo.save_books(books_to_save)