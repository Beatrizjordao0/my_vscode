'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Creating our Database and Table 
'''

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
mycursor.execute('SELECT * FROM students')

for tb in mycursor:
    print(tb)

# 1- CREATE DATABASE nome_do_banco_de_dados
# 2- SHOW DATABASE
# 3- CREATE TABLE students(name VARCHAR(255), age INT(10))
# 4- SHOW TABLES

