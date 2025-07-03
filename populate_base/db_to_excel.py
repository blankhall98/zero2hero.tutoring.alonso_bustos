import pandas as pd
from db import get_engine

engine = get_engine()

sql_dataframe = pd.read_sql_table('base',engine)

#Write it out to Excel
sql_dataframe.to_excel('./clean_data/registros.xlsx', index=False)