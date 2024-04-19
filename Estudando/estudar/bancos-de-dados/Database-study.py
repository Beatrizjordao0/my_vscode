import mysql.connector

# initialize the database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2233287774449999',
    database='testdb'            # We use this to select the database we want to work with
)
# this is how python conects with mysql.
# this database cursor is like an input on command prompt

mycursor = mydb.cursor()

# every statement I make to create a database and tables on the command prompt
# will be made here ↓
mycursor.execute('SHOW DATABASES')

# 1- CREATE DATABASE nome_do_banco_de_dados
# 2- SHOW DATABASE


for db in mycursor:
    print(db)
