from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, Integer, String, DateTime, func, UniqueConstraint
#crear una base declarativa
Base = declarative_base()


#definicion de modelos
class BaseMixin:
    """Mixin para añadir columnas comunes."""
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        onupdate=func.now(), server_default=func.now())

    #Definicion del modelo User
class Usuario(BaseMixin, Base):
    __tablename__ = "usuarios"
    nombre = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False, unique=True)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}')>"