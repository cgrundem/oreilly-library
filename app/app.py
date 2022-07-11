from crypt import methods
from flask import Flask, request
import sys
from flaskext.mysql import MySQL
import os
import logging
import json

sys.path.insert(0, "..")

from services.books.book_metadata_repo import BookMetadataRepository
from services.books.book_metadata_service import BookMetadataService
from services.books.book_query_factory import BookQueryFactory

from services.api.oreilly_api_client import OReillyAPIClient

from services.mysql_repository import MySqlRepository

#logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)

mysql = MySQL()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "password"
app.config["MYSQL_DATABASE_DB"] = "BookLibrary"
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)

my_sql_repository: MySqlRepository = MySqlRepository("0.0.0.0", 3306, "password", "BookLibrary")

book_query_factory: BookQueryFactory = BookQueryFactory()


_book_metadata_repository: BookMetadataRepository = BookMetadataRepository(mysql.connect(), book_query_factory)
_book_metadata_service: BookMetadataService = BookMetadataService(_book_metadata_repository, book_query_factory, OReillyAPIClient())

@app.route("/load")
def etl_books():
    return json.dumps(_book_metadata_service.extract_and_load_books({
            "title": "python"
          }), default=str)

@app.route("/add", methods=["POST"])
def add_book():
    request_data = request.get_json()
    _book_metadata_service.save_books([request_data])
    return "successfully added book"
  
@app.route("/all", methods=["GET"])
def get_all_books():
  return json.dumps(_book_metadata_service.get_all_books(), default=str)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')