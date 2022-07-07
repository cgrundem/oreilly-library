from services.mysql_repository import MySqlRepository
from services.books.book_query_factory import BookQueryFactory
import urllib.parse
import requests

class BookMetadataRepository:
  def __init__(self, mysql_repository: MySqlRepository, book_query_factory: BookQueryFactory):
    self._mysql_repo: MySqlRepository = mysql_repository
    self._book_query_factory: BookQueryFactory = book_query_factory

  def find_books_by_search_query(self, query):
    def make_oreilly_query_request_model(q):
      result = ""
      
      if "title" in query and query["title"]:
        result += "title:" + urllib.parse.quote(query["title"]) + " "
      if "author" in query and query["author"]: 
        result += "author:" + urllib.parse.quote(query["author"]) + " "
      if "isbn" in query and query["isbn"]:
        result += "archive_id:" + urllib.parse.quote(query["isbn"]) + " "
      print(result)
      #safe_string = urllib.parse.quote_plus()
      return result.rstrip()
    url = f"https://learning.oreilly.com/api/v2/search/?query={make_oreilly_query_request_model(query)}"
    response = requests.get(url)
    return response.json()["results"] if response and "results" in response.json() and response.json()["results"] else None
    
        
  def find_books_by_search_query_mysql(self, query):
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