import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Bibiperigosa",
        password="123456789",
        database="GerenciadorDeTarefas"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print("Erro ao conectar ao banco de dados:", err)
