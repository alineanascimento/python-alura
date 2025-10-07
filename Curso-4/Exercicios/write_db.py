import sqlite3


conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

#SQL INJETION (? , ?) p/ proteger os dados
cursor.execute(
    """
       INSERT INTO estudantes(nome, idade) \
        VALUES (?, ?)
        
    """,
    ("Joana", 16)
)


cursor.execute(
     """
         INSERT INTO disciplinas(estudante_id, nome_disciplina) \
         VALUES (?, ?)
        
     """,
     (1, "Matemática")
 )




conn.commit()

conn.close()