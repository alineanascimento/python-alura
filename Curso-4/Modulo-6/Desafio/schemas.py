from email.policy import strict
from pydantic import BaseModel, StrictInt # adicionar para validação 

# Estudante
class EstudanteBase(BaseModel): # criado como molde p/ entra e saida 
    nome: str
    idade: StrictInt
    email: str


#Adiciona o campo que só faz sentido na criação (cadastro).
class EstudanteCreate(EstudanteBase):
    senha: str


#Define o que o servidor devolve ao cliente.
class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_attributes = True

