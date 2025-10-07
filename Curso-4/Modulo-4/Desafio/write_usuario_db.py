import sqlite3

dados_usuarios = [("Beatriz", "bia@hotmail.com"), ("Ana", "ana@hotmail.com")]


conn = sqlite3.connect("usuario.db")
cursor = conn.cursor()

#SQL INJETION (? , ?) p/ proteger os dados
for dados in dados_usuarios:
    cursor.execute(
        """
        INSERT INTO usuarios (nome, email) \
            VALUES (?, ?)
            
        """,
        (dados)
    )

conn.commit()

conn.close() 
