# read_raw.py

import pandas as pd
from config import config

df = pd.read_excel(config['raw_path']+config['filename'])

# create database
from sqlalchemy import create_engine

engine = create_engine(config['DATABASE_URL'])

#create table
df.to_sql("rendimientos_fibras", engine, if_exists="replace", index=False)

#inside python query
query = """
SELECT * FROM rendimientos_fibras 
WHERE "Fecha" > '2024-08-15'
ORDER BY "Fecha" DESC
LIMIT 10;
"""
sub_base = pd.read_sql(query,engine)