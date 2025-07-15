# analysis.py
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from config import config

# Crear conexión
engine = create_engine(config['DATABASE_URL'])

# Query: solo la fibra P_FUNO
query = """
SELECT "Fecha", "Rend_FUNO"
FROM rendimientos_fibras
WHERE "P_FUNO" IS NOT NULL
ORDER BY "Fecha";
"""

# Leer los datos a un DataFrame
df = pd.read_sql(query, engine)

# Convertir la columna fecha a datetime y establecer como índice
df['Fecha'] = pd.to_datetime(df['Fecha'])
df.set_index('Fecha', inplace=True)

print(df.describe())

# Histograma y boxplot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Rend_FUNO'], kde=True)
plt.title('Distribución de P_FUNO')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Rend_FUNO'])
plt.title('Boxplot de P_FUNO')
plt.tight_layout()
plt.show()

#time series graph
plt.figure(figsize=(12, 4))
df['Rend_FUNO'].plot(title='Serie de Tiempo: Rend_FUNO')
plt.ylabel('Rendimiento (%)')
plt.xlabel('Fecha')
plt.grid(True)
plt.show()

#Estacionariedad: Test de Dickey-Fuller Aumentado (ADF)
resultado_adf = adfuller(df['Rend_FUNO'].dropna())
print('Estadístico ADF:', resultado_adf[0])
print('p-valor:', resultado_adf[1])
print('Valores críticos:', resultado_adf[4])

if resultado_adf[1] < 0.05:
    print("✅ La serie es estacionaria.")
else:
    print("⚠️ La serie NO es estacionaria.")
    
#ACF y PACF (para identificar orden del modelo ARIMA)
plot_acf(df['Rend_FUNO'].dropna(), lags=20)
plt.title('Autocorrelación (ACF)')
plt.show()

plot_pacf(df['Rend_FUNO'].dropna(), lags=20)
plt.title('Autocorrelación Parcial (PACF)')
plt.show()

#Modelado Arima
from statsmodels.tsa.arima.model import ARIMA

# ARIMA(p=1, d=1, q=1) como ejemplo
modelo = ARIMA(df['Rend_FUNO'], order=(1, 1, 1))
modelo_fit = modelo.fit()

# Resumen del modelo
print(modelo_fit.summary())

# Número de pasos a predecir
n_forecast = 50

# Obtener fechas futuras
last_date = df.index[-1]
future_dates = pd.date_range(start=last_date, periods=n_forecast + 1, freq='D')[1:]

# Hacer predicción
pred = modelo_fit.predict(start=len(df), end=len(df)+n_forecast-1, typ='levels')

# Crear un DataFrame con las predicciones y su índice
forecast_df = pd.DataFrame({'Pronóstico': pred})
forecast_df.index = future_dates

# Graficar
plt.figure(figsize=(10, 4))
df['Rend_FUNO'].plot(label='Observado')
forecast_df['Pronóstico'].plot(label='Pronóstico', linestyle='--')
plt.title('Pronóstico ARIMA')
plt.xlabel('Fecha')
plt.ylabel('Rendimiento')
plt.legend()
plt.grid(True)
plt.show()


