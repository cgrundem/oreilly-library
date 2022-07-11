import urllib.parse

class BookQueryFactory:
  def __init__(self):
    pass

  def make_mysql_query_string_from_query(self, query_conditions, table_name, fields=[]):
    mysql_query_string = f"SELECT {','.join(fields) if fields else '*'} FROM {table_name} WHERE "
    return mysql_query_string + query_conditions
    
  def make_condition_string(self, condition_tuples):
    result = ""
    for i in range(len(condition_tuples)):
      condition, op = condition_tuples[i]
      if condition_tuples[i] != condition_tuples[-1]:
        result += f"{condition} {op}"
      else:
        result += condition
    return result
    
  def make_oreilly_query_request_model(self, query):
      result = ""
      
      if "title" in query and query["title"]:
        result += "title:" + urllib.parse.quote(query["title"]) + " "
      if "author" in query and query["author"]: 
        result += "author:" + urllib.parse.quote(query["author"]) + " "
      if "isbn" in query and query["isbn"]:
        result += "archive_id:" + urllib.parse.quote(query["isbn"]) + " "
      return result.rstrip()