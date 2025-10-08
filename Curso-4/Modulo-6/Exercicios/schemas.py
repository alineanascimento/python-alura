from pydantic import BaseModel 

#validacao
class EstudanteBase(BaseModel):
    nome: str
    idade: int

#campos sao os mesmos do estudanteBase, entao nao precisa repetir
class EstudanteCreate(EstudanteBase):
    pass

#significa que pode ler direto da classe
class EstudanteResponse(EstudanteBase):
    id: int
    class Config:
        from_attributes = True


class MatriculaBase(BaseModel):
    estudante_id = int
    nome_disciplina = str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes = True