import pymysql

myDatabase = pymysql.connect(
host="localhost",
user="root",
password="",
database="airport_database"
)

print("DATABASE CONNECT WELL.")
mycursor = myDatabase.cursor()
