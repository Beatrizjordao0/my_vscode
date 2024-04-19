'''
the codex - Youtube Class
19/04/2024
Python and MySQL - Populating our Database and Table
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

# Populating the database is just to add data to the database
sqlFormula = 'INSERT INTO students (name, age) VALUES (%s, %s)'
# student_1 = ('Dahvi', 6)
students = [('Bob',48),
            ('Thomas',7),
            ('Sheila',44),
            ('Larissa',24),
            ('Beatriz',17),
            ('Fernando',44),
            ('Margareth',67)]

# mycursor.execute(sqlFormula, students)
mycursor.executemany(sqlFormula, students)

mydb.commit()