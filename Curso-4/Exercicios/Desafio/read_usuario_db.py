import sqlite3


conn = sqlite3.connect("usuario.db")
cursor = conn.cursor()

#consulte todas as ocorrencias da tabela estudantes sem nenhum filtro
cursor.execute(
    """
        SELECT * FROM usuarios
    """
)
usuarios = cursor.fetchall()
print(usuarios)


conn.commit()