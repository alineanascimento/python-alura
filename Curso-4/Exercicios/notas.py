import csv

dict_notas = {"Aline": 10, "Ana": 5, "Luis": 9, "Fabio": 6, "Alex": 6, "Felipe": 8}

# Gravar os dados no arquivo CSV
with open("alunos.csv", "w", newline="", encoding="utf-8") as f:
    escrita = csv.writer(f)
    escrita.writerow(["Nome", "Nota"])  # cabeçalho
    for nome, nota in dict_notas.items():
        escrita.writerow([nome, nota])

print("Alunos com nota maior ou igual a 7.0:\n")

with open("alunos.csv", newline="", encoding="utf-8") as f:
    leitura = csv.reader(f)
    next(leitura)  # pula o cabeçalho
    for linha in leitura:
        nome, nota = linha
        if int(nota) >= 7.0:
            print(f"{nome}: {nota}")
