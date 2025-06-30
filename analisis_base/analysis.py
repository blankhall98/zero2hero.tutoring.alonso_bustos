# analysis.py

# Import Libraries
import pandas as pd #pandas: manejo de bases de datos
import numpy as np #numpy: analisis numerico
import matplotlib.pyplot as plt #matplotlib: graficas y figuras
import statsmodels.api as sm

# Routes Dictionary
routes = {
    'raw data': './data/raw_data/',
    'clean data': './data/clean_data/',
    'output': './output/'
    }

# Read Excel File
filename = 'Base_edos.xlsx'
data = pd.read_excel(routes['raw data']+filename)

# Base Shape Analysis
print(data.shape)

# first n elements
print(data.head(10))

# describe base
print(data.describe())

# print columns
print(data.columns)

########

#Query: create sub-base by state
state = 'Aguascalientes'
sub_base = data[data['Estado']==state]

sub_base_not_null = data[(data['Estado']==state)&(data['Sucursales']!=0)]

condition = (data['Estado'].isin(['Aguascalientes','Chiapas','Oaxaca']))&(data['Sucursales']!=0)

query = data[condition]

#######

#histogram
plt.figure()
plt.hist(data['Sucursales'],bins=100)
plt.show()

#histogram using pandas
data['Cajeros'].hist(bins=100)
plt.show()

# Histograms for each numerical column
#    adjust bins or figsize to taste
data.hist(bins=25, figsize=(12, 8))
plt.tight_layout()
plt.show()

#linear regression
y = data['Tarjetas de Crédito (TDC)']
x = data[['Superficie km2','Población Adulta','Sucursales','Cajeros']]
x = sm.add_constant(x)

#quick fix: fix superfice column
def reparar_numero(x):
    txt = str(x)
    partes = txt.split('.')
    if len(partes) <= 2:
        return txt               # 0 o 1 punto: ya está bien
    entero = ''.join(partes[:-1])  # junta todo salvo el último punto
    decimal = partes[-1]
    return entero + '.' + decimal

data['Superficie km2'] = data['Superficie km2'].apply(reparar_numero)
data['Superficie km2'] = pd.to_numeric(data['Superficie km2'], errors='coerce')

x_numeric = x.apply(lambda col: pd.to_numeric(col, errors='coerce'))
y_numeric = pd.to_numeric(y, errors='coerce')

mask = x_numeric.notna().all(axis=1) & y_numeric.notna()
x = x_numeric.loc[mask]
y = y_numeric.loc[mask]

model = sm.OLS(y,x).fit()

#Extract and round coefficients & p-values to 3 sig figs
coef_table = pd.DataFrame({
    'coef': model.params,
    'pval':  model.pvalues
}).applymap(lambda x: float(np.format_float_positional(x, precision=3, unique=False, fractional=False)))
print(coef_table)

#save summary as pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# 1) Get the text of your summary
summary_str = model.summary().as_text()
lines = summary_str.split('\n')

# 2) Create a PDF and start writing text
c = canvas.Canvas("model_summary.pdf", pagesize=letter)
width, height = letter
text_obj = c.beginText(40, height - 40)
text_obj.setFont("Courier", 9)

# 3) Write each line (you may need to manage page breaks if it's long)
for line in lines:
    if text_obj.getY() < 40:          # if near bottom, start a new page
        c.drawText(text_obj)
        c.showPage()
        text_obj = c.beginText(40, height - 40)
        text_obj.setFont("Courier", 9)
    text_obj.textLine(line)

# 4) Finish up
c.drawText(text_obj)
c.save()






