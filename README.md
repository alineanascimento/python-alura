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


📂 **Código:** [`/Curso-2`](Curso-2)

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
