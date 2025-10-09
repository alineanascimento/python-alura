from typing import List, Optional
from pydantic import BaseModel


# PERFIL

class PerfilBase(BaseModel):
    idade: int
    endereco: str


class PerfilCreate(PerfilBase):
    pass


class Perfil(PerfilBase):
    id: int

    class Config:
        from_attributes = True


# ESTUDANTE

class EstudanteBase(BaseModel):
    nome: str
    email: str


class EstudanteCreate(EstudanteBase):
    perfil: PerfilCreate


class Estudante(EstudanteBase):
    id: int
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True



# DISCIPLINA

class DisciplinaBase(BaseModel):
    nome: str
    descricao: str


class DisciplinaCreate(DisciplinaBase):
    pass


class Disciplina(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True



# MATRÍCULA

class MatriculaBase(BaseModel):
    estudante_id: int
    disciplina_id: int


class MatriculaCreate(MatriculaBase):
    pass


class Matricula(MatriculaBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


# PROFESSOR

class ProfessorBase(BaseModel):
    nome: str


class ProfessorCreate(ProfessorBase):
    pass


class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True
