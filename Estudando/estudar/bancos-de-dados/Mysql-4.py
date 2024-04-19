'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Query Conditions with WHERE and Wildcards
'''

import mysql.connector
# initialize the database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2233287774449999',
    database='testdb'
)

mycursor = mydb.cursor()

# sqlCommand = 'SELECT * FROM students WHERE name = "Sheila"'

                     # LIKE is something close to this ↓
sqlCommand = 'SELECT * FROM students WHERE name LIKE "%Th%" ' # we give it part of the name, and it returns for us
                                                             # names that looks like what we gave to it
                        
mycursor.execute(sqlCommand)

for age in mycursor:
    print(age)