from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer)
    email = Column(String(100))
    senha = Column(String(100))