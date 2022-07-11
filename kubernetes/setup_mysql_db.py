import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE BookLibrary")

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="password",
  database="BookLibrary"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE book_metadata (guid CHAR(36) PRIMARY KEY, title VARCHAR(100), author VARCHAR(100), isbn CHAR(13), description VARCHAR(1000), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


