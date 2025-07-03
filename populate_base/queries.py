from db import get_engine, get_session
from models import Data
from sqlalchemy import func

session = get_session(get_engine())

'''
# 1. Todos los registros

# SELECT * FROM base
todos = session.query(Data).all()
ahorro_total = 0
for obs in todos:
    ahorro_total += obs.ahorro
print(f'ahorro total {ahorro_total}')
'''

# 2. Filtrar por categoría
cat = 'Aguascalientes'
min_sucursal = 1
result = session.query(Data).filter(Data.estado == cat, Data.sucursales >= min_sucursal).all()
ahorro_total = 0
for obs in result:
    ahorro_total += obs.ahorro
print(f'ahorro total {ahorro_total}')