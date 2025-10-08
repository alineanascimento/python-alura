from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# cria as tabelas no PostgreSQL (caso nao exista)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudantes/", response_model = schemas.EstudanteResponse)

def create_student(student: schemas.EstudanteCreate, db: Session=Depends(get_db)):
    db_student = models.Estudante(**student.model_dump) # objeto do modelo estudante com as informacoes do meu navegador 
    # model_dump converte json em dict
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# rota pra buscar informações, não tem problema ser a mesma do post
@app.get("/estudantes/", response_model = List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_db())):
    students = db.query(models.Estudante).all()
    return students

# DESAFIO  = Rota para buscar um estudante específico pelo ID
@app.get("/estudantes/{estudante_id}", response_model=schemas.EstudanteResponse)
def read_student(estudante_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return student



@app.post("/matriculas/", response_model = schemas.MatriculaResponse)

def create_registration(registration: schemas.MatriculaCreate, db: Session=Depends(get_db)):
    db_registration = models.Matricula(**registration.model_dump) 
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration


@app.get("/matriculas/", response_model = List[schemas.MatriculaResponse])
def read_registrations(db: Session = Depends(get_db())):
    registrations = db.query(models.Matricula).all()
    return registrations

