#En este archivo leemos el excel, y fila por fila poblamos la base de datos

#Importamos las bibliotecas
import pandas as pd
from db import get_engine, init_db, get_session
from models import Data

def main():
    
    # 1. Lee el Excel
    df = pd.read_excel('./data/data.xlsx')
    
    # 2. Conecta y crea tablas
    engine = get_engine()
    init_db(engine)
    session = get_session(engine)
    
    # 3. Convierte filas de pandas a instancias ORM
    registro = []
    for _,row in df.iterrows():
        new_row = Data(
            estado = row['Estado'],
            poblacion_adulta = row['Población Adulta'],
            sucursales = row['Sucursales'],
            tdc = row['Tarjetas de Crédito (TDC)'],
            ahorro = row['Cuentas ahorro']
            )
        registro.append(new_row)
        
    # 4. Inserta en bloque
    session.bulk_save_objects(registro)
    session.commit()
    print(f"Insertados {len(registro)} registros.")
    
    return df, registro
    
if __name__ == '__main__':
    df, registro = main()

