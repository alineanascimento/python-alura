from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Cria as tabelas no PostgreSQL (caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  Criar estudante
@app.post("/estudantes/", response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    # Converte o corpo da requisição (JSON) para dict com model_dump()
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Buscar estudante específico pelo ID (DESAFIO)
@app.get("/estudantes/{estudante_id}", response_model=schemas.EstudanteResponse)
def read_student(estudante_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return student


# Listar todos os estudantes 
@app.get("/estudantes/", response_model=List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students
