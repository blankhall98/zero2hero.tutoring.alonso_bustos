from models import Usuario
from app import get_session

'''
#CREATE
with get_session() as session:
    nuevo = Usuario(nombre='Jonatan',email='blankhall@gmail.com')
    session.add(nuevo)
'''

#READ
with get_session() as session:
    usuario = session.query(Usuario).all()
    