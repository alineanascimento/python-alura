import sqlite3

conn = sqlite3.Connection("usuario.db")

cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        
        ) 

    """
)

conn.commit()

conn.close()