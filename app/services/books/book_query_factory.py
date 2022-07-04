

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
    