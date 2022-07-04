#from MySQLdb import _mysql


class MySqlRepository:
  def __init__(self, host, port, password, database_name):
    # self._context = _mysql.connect(host=host,port=port,passwd=password,db=database_name)
    pass
  def query(self, q):
    return {
      "author": "demarcus cousins",
      "title": "Great Expectations",
      "description": "2022 remake",
      "isbn": "9781234567897"
    }
    #return self._context.query(q).store_result().fetch_row()

