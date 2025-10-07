import sqlite3


conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

#consulte todas as ocorrencias da tabela estudantes sem nenhum filtro
#cursor.execute(
#    """
#        SELECT * FROM estudantes
#    """
#)

cursor.execute(
    """
        SELECT * FROM disciplinas
    """
)


conn.commit()


disciplinas = cursor.fetchall()
for disciplina in disciplinas:
    print(disciplina)

#estudantes = cursor.fetchall() # salva tudo que ele achou na variavel estudantes

# for estudante in estudantes:
#     print(estudante)
# pra comentar de uma vez ctrl + k  ctrl + c


conn.close()