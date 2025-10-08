from pydantic import BaseModel

# Estudante
class EstudanteBase(BaseModel):
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_attributes = True

