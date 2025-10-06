import sqlite3

conn = sqlite3.connect("escola.db") # conecta, verifica se existe o banco de dados, caso nao, cria um
cursor = conn.cursor() # cursor pra  executar tarefas no banco de dados

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", ("João", 20))

conn.commit()

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

conn.close()
