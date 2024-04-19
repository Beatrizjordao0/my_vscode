
import mysql.connector

mydb = mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='2233287774449999'           # We use this to select the database we want to work with
)
mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE students')

for db in mycursor:
    print(db)