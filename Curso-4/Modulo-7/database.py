from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com o MySQL
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/db_colegio"

# Cria o engine de conexão
engine = create_engine(
    DATABASE_URL,
    echo=True,             # Mostra as queries SQL no terminal (ótimo pra debug)
    pool_pre_ping=True     # Evita erros de conexão inativa
)

# Cria sessão para as transações (insert, select, update, delete)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base do ORM (todas as tabelas herdam dela)
Base = declarative_base()
