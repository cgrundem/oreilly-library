from services.mysql_repository import MySqlRepository
from services.books.book_query_factory import BookQueryFactory

class BookMetadataRepository:
  def __init__(self, mysql_repository: MySqlRepository, book_query_factory: BookQueryFactory):
    self._mysql_repo: MySqlRepository = mysql_repository
    self._book_query_factory: BookQueryFactory = book_query_factory

  def find_books_by_search_query(self, query):
    condition_tuples = []
    
    if "title" in query and query["title"]:
      condition_tuples.append((f"title = {query['title']}", "AND"))
    if "author" in query and query["author"]:
      condition_tuples.append((f"author = {query['author']}", "AND"))
    if "isbn" in query and query["isbn"]:
      condition_tuples.append((f"isbn  = {query['isbn']}", "OR"))

    query_conditions: str = self._book_query_factory.make_condition_string(condition_tuples)
    result = self._book_query_factory.make_mysql_query_string_from_query(query_conditions, [])

    return result