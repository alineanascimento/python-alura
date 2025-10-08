from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com PostgreSQL
# Formato: postgresql://usuario:senha@localhost:porta/nome_do_banco
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/escola"

# Cria o mecanismo de conexão (engine)
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()
