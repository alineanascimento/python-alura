from sqlalchemy import Column, String, Integer, ForeignKey, Text, CHAR
from sqlalchemy.orm import relationship
from database import Base


# Tabela: Professor
class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100, collation="utf8mb4_general_ci"), nullable=False)

    # Relacionamento 1:N -> Estudantes
    estudantes = relationship(
        "Estudante",
        back_populates="professor",
        cascade="all, delete-orphan"
    )



# Tabela: Estudante

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100, collation="utf8mb4_general_ci"), nullable=False)
    email = Column(String(120, collation="utf8mb4_general_ci"), unique=True, nullable=False)

    # FK professor
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=True)
    professor = relationship("Professor", back_populates="estudantes")

    # Relacionamentos
    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan"
    )
    matriculas = relationship(
        "Matricula",
        back_populates="estudante",
        cascade="all, delete-orphan"
    )


# Tabela: Perfil (1:1 com Estudante)
class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idade = Column(Integer, nullable=True)
    endereco = Column(String(200, collation="utf8mb4_general_ci"))

    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True, nullable=False)
    estudante = relationship("Estudante", back_populates="perfil")


# Tabela: Disciplina
class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100, collation="utf8mb4_general_ci"), nullable=False)
    descricao = Column(Text(collation="utf8mb4_general_ci"), nullable=False)

    matriculas = relationship(
        "Matricula",
        back_populates="disciplina",
        cascade="all, delete-orphan"
    )


# Tabela: Matricula (N:N entre Estudante e Disciplina)
class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"), nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)

    estudante = relationship("Estudante", back_populates="matriculas")
    disciplina = relationship("Disciplina", back_populates="matriculas")