from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def get_engine(path='sqlite:///data.db'):
    # Usa SQLite local; cambia por otra URL si prefieres PostgreSQL, MySQL, etc.
    return create_engine(path, echo=False)

def init_db(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
