from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

# Cria as tabelas no banco (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência do banco 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ROTAS DE ESTUDANTES 
@app.post("/estudantes/", response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())  # <- precisa dos parênteses
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/estudantes/", response_model=List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students


# ROTAS DE MATRÍCULAS 
@app.post("/matriculas/", response_model=schemas.MatriculaResponse)
def create_registration(registration: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_registration = models.Matricula(**registration.model_dump())
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration


@app.get("/matriculas/", response_model=List[schemas.MatriculaResponse])
def read_registrations(db: Session = Depends(get_db)):
    registrations = db.query(models.Matricula).all()
    return registrations
