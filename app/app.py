from flask import Flask
import sys

sys.path.insert(0, "..")

from services.books.book_metadata_repo import BookMetadataRepository
from services.books.book_metadata_service import BookMetadataService
from services.books.book_query_factory import BookQueryFactory

from services.mysql_repository import MySqlRepository

app = Flask(__name__)

my_sql_repository: MySqlRepository = MySqlRepository("localhost", 3306, "password", "books")

book_query_factory: BookQueryFactory = BookQueryFactory()


_book_metadata_repository: BookMetadataRepository = BookMetadataRepository(my_sql_repository, book_query_factory)
_book_metadata_service: BookMetadataService = BookMetadataService(_book_metadata_repository)

@app.route("/")
def hello():
    return {
      "books": 
          _book_metadata_service.find_books_by_search_query({
            "author": "robert martin",
            "title": "clean code"
          })
    }
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')