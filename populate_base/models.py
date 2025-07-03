from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date

Base = declarative_base()

class Data(Base):
    
    __tablename__ = "base"
    id = Column(Integer, primary_key=True)
    estado = Column(String(120),nullable=True)
    poblacion_adulta = Column(Float,nullable=True)
    sucursales = Column(Integer,nullable=True)
    tdc = Column(Float,nullable=True)
    ahorro = Column(Float,nullable=True)
    
    def __repr__(self):
        return f"{self.estado}"
    