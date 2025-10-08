<h1 align="center">
  🐍 Formação Python - Alura
</h1>

---

## 🎯 Sobre o Repositório

Este repositório reúne todos os **projetos da formação de Python da Alura**, organizados por curso.  
Cada pasta representa uma etapa de aprendizado, com evolução gradual — do primeiro programa em Python até a criação de uma API completa com FastAPI.

---

## 🧩 Curso 1 — Python: Crie a sua Primeira Aplicação

📌 **Descrição:**  
Desenvolvimento de um sistema de gerenciamento de restaurantes via terminal.

🧠 **Conceitos principais:**
- Estruturas condicionais e de repetição (`if`, `for`, `while`)
- Listas, dicionários e funções com docstrings
- Manipulação de entradas do usuário (`input()`)
- Exibição formatada com f-strings
- Tratamento de exceções com `try/except`
- Limpeza de tela com `os.system("cls")`

💻 **Funcionalidades:**
- Cadastrar, listar e ativar/desativar restaurantes  
- Menu interativo no console  
- Exibição organizada com subtítulos formatados  

---

## ⚙️ Curso 2 — Python: Aplicando a Orientação a Objetos

📌 **Descrição:**  
Reestruturação completa do sistema de restaurantes utilizando **Programação Orientada a Objetos (POO)**.

🧠 **Conceitos principais:**
- Criação de **classes e objetos**
- Construtor (`__init__`) e representação (`__str__`)
- Atributos protegidos (`_atributo`) e encapsulamento com `@property`
- Herança e uso de `super()`
- Classes e métodos abstratos (`from abc import ABC, abstractmethod`)
- Modularização e importação de arquivos (`from arquivo import Classe`)

---

## 🌐 Curso 3 — Python: Avance na Orientação a Objetos e Consuma uma API

📌 **Descrição:**  
Criação de uma **API de cardápios de restaurantes** com FastAPI, consumindo dados reais de uma API externa.

🧠 **Conceitos principais:**
- Introdução ao **FastAPI** e **Uvicorn**
- Criação de endpoints (`@app.get`)
- Uso de **Query Parameters** para filtros
- Consumo de API externa com `requests`
- Manipulação e gravação de dados **JSON**
- Organização de respostas estruturadas

💻 **Exemplo de endpoint:**
```python
@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    ...

---

🌐 **Curso 4 — Python: Persistência de Dados com Arquivos, Bancos de Dados e APIs REST**

📌 **Descrição:**  
Desenvolvimento de aplicações Python capazes de **armazenar e recuperar informações** utilizando **arquivos (.txt, .csv, .json)** e **bancos de dados relacionais e não relacionais (SQLite, PostgreSQL e MongoDB)**.  
Ao final, o projeto integra **FastAPI** e **PostgreSQL** para criar uma **API REST completa** com operações CRUD.

🧠 **Conceitos principais:**
- Estruturas de dados: **listas, tuplas e dicionários**  
- Leitura e gravação de arquivos em **.txt**, **.csv** e **.json**  
- Diferenças entre **bancos de dados relacionais (SQL)** e **não relacionais (NoSQL)**  
- Criação e manipulação de tabelas no **SQLite** com o módulo `sqlite3`  
- Prevenção de **SQL Injection** e boas práticas de segurança  
- Integração do **Python com o SQLite** usando funções  
- Introdução à **API REST** e métodos **HTTP (GET, POST, PUT, DELETE)**  
- Persistência com **PostgreSQL** e integração via **FastAPI + SQLAlchemy + Pydantic**  
- Criação de **modelos**, **schemas** e **endpoints** para CRUD  
- Execução e testes com **Uvicorn** e **Swagger UI**

📁 **Exemplo prático — Integração Python + SQLite:**

```python
import sqlite3

def conectar():
    return sqlite3.connect("escola.db")

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """)
    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes")
    for linha in cursor.fetchall():
        print(linha)
    conn.close()

# Execução
criar_tabela_estudantes()
criar_estudante("Aline", 22)
listar_estudantes()
