from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

import models, schemas
from database import engine, SessionLocal

# Inicializa a aplicação e o banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Escolar", version="1.0.0")



# Dependência de sessão

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# ROTAS: ESTUDANTES

@app.post("/estudantes/", response_model=schemas.Estudante, status_code=201)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        perfil=models.Perfil(**estudante.perfil.model_dump())
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante


@app.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return estudantes



# ROTAS: DISCIPLINAS

@app.post("/disciplinas/", response_model=schemas.Disciplina, status_code=201)
def criar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    db_disciplina = models.Disciplina(**disciplina.model_dump())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina


@app.get("/disciplinas/", response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(models.Disciplina).all()


# ROTAS: PROFESSORES

@app.post("/professores/", response_model=schemas.Professor, status_code=201)
def criar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(**professor.model_dump())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor


@app.get("/professores/", response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()


# ROTAS: MATRÍCULAS
@app.post("/matriculas/", response_model=schemas.Matricula, status_code=201)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    estudante = db.get(models.Estudante, matricula.estudante_id)
    disciplina = db.get(models.Disciplina, matricula.disciplina_id)

    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")

    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@app.get("/matriculas/", response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()
