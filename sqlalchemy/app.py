
from config import engine
from sqlalchemy.ext.declarative import declarative_base
    
########################################################################
Base = declarative_base()
Base.metadata.create_all(bind=engine)

########################################################################
from contextlib import contextmanager
from config import SessionLocal

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
########################################################################
