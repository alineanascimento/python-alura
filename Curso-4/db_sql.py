import sqlite3

conn = sqlite3.connect("escola.db") # conecta, verifica se existe o banco de dados, caso nao, cria um
cursor = conn.cursor() # cursor pra  executar tarefas no banco de dados

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
)
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) \
                REFERENCES estudantes(id)
        )
    """
)

conn.commit() # confirma a execução
 
conn.close() # fecha a conexao