import requests

class OReillyAPIClient:
    def __init__(self):
      pass
    
    def transform_book_query_response(self, book_results):
        return [{
            "title": book["title"] if "title" in book and book["title"] else "",
            "author": '|'.join(book["authors"]) if "authors" in book and book["authors"] else "",
            "description": book["description"] if "description" in book and book["description"] else "",
            "isbn": book["archive_id"] if "archive_id" in book and book["archive_id"] else ""
        } for book in book_results]
    
    def get_books_test(self, query):
        url = f"https://learning.oreilly.com/api/v2/search/?query={query}"
        response = requests.get(url)
        response_results = response.json()["results"] if response and "results" in response.json() and response.json()["results"] else None
        if not response_results:
          return []
        return self.transform_book_query_response(response_results)
