import sqlite3


conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

#consulte todas as ocorrencias da tabela estudantes sem nenhum filtro
#cursor.execute(
#    """
#        SELECT * FROM estudantes
#    """
#)

# cursor.execute(
#     """
#         SELECT * FROM disciplinas
#     """
# )

# cursor.execute(
#     """
#         SELECT * FROM estudantes WHERE id = 1
#     """
# )

cursor.execute(
    """
        SELECT estudantes.nome, disciplinas.nome_disciplina FROM disciplinas \
              JOIN estudantes ON disciplinas.estudante_id
    """
)




estudante = cursor.fetchall()
print(estudante)


conn.commit()


# disciplinas = cursor.fetchall()
# for disciplina in disciplinas:
#     print(disciplina)

#estudantes = cursor.fetchall() # salva tudo que ele achou na variavel estudantes

# for estudante in estudantes:
#     print(estudante)
# pra comentar de uma vez ctrl + k  ctrl + c


