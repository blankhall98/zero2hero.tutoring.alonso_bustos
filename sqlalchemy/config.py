# config.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

# echo=True para ver el SQL generado
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_size=10,            # número de conexiones en el pool
    max_overflow=20,         # conexiones extra si pool lleno
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,         # no hace flush automático antes de queries
    autocommit=False,        # controla commits manualmente
    expire_on_commit=False   # evita expirar atributos tras commit
)


