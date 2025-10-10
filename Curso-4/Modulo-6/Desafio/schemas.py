from pydantic import BaseModel

# Estudante
class EstudanteBase(BaseModel): # criado como molde p/ entra e saida 
    nome: str
    idade: int
    email: str


#Adiciona o campo que só faz sentido na criação (cadastro).
class EstudanteCreate(EstudanteBase):
    senha: str


#Define o que o servidor devolve ao cliente.
class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_attributes = True

