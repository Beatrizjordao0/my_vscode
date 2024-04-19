import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2233287774449999',
    database='testdb'
)

mycursor = mydb.cursor()

              # name of the table = ↓      ↓ = statement1     ↓ = statement2
# mycursor.execute('CREATE TABLE students(name VARCHAR(255), age INT(10))')
                                    # type ↑             type ↑

mycursor.execute('SHOW TABLES')

for tb in mycursor:
    print(tb)
