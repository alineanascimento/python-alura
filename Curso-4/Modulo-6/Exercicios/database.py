from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

#usuario:senha
DATABASE_URL = "postgresql://postgres:postgres@localhost/escola"

#motor do banco de dados, o que vai comunicar o banco de dados com o FastAPI 
engine = create_engine(DATABASE_URL)
#cria uma conexao temporaria com o banco de dados
SessionLocal = sessionmaker(bind=engine)
# cria as nossas entidades
Base = declarative_base()