from conexion_pg import  db_url
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine, MetaData, Table, desc
from datetime import datetime, timedelta

# Crear el motor de la base de datos
engine = create_engine(db_url)

# Crear el objeto metadata
metadata = MetaData()

# Obtener la tabla 'historico'
historico = Table('historico', metadata, autoload_with=engine)

# Realizar la consulta (Con orden descendente limitando a 1 el resultado obtenemos la última fecha)
resultados = engine.execute(historico.select().order_by(desc(historico.c.Date)).limit(1)).fetchall()

# Imprimir los resultados
for resultado in resultados:
   print("Fecha de última actualización: " + resultado[0])

lista_tickers = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'NFLX', 'TSLA', 'META', 'AMD', 'XOM', 'UBER', 'QCOM', 'COIN', 'KO', 'BAC', 'HD', 'PYPL', 'JPM', 'UNH', 'V']

start_ticker = resultado[0] + timedelta(days=1)

end_ticker = datetime.now().date()

data = pd.DataFrame()

for ticker in lista_tickers:
    tick0 = yf.Ticker(ticker)
    data_ticker = pd.DataFrame(tick0.history(start=start_ticker, end=end_ticker))
    data_ticker['Ticket'] = ticker
    data_ticker = data_ticker.reset_index()
    data = pd.concat([data, data_ticker], ignore_index=True)

historico = pd.DataFrame(data)
historico['Date'] = pd.to_datetime(historico['Date']).dt.date
print(historico)
# Convertir el dataframe a un formato compatible con PostgreSQL

if str(historico['Date'].tail(1).iloc[0]) > str(resultado[0]):
  try:
    historico.to_sql(
        name='historico',
        con=engine,
        schema='public',
        if_exists='append',
        index=False
    )
  except Exception as e:
      print("Error al conectar a la base de datos:", e)
  finally:
      # Cierra la conexión
      engine.dispose()
      print("Conexión cerrada.")
else:
  print("Sin datos nuevos")

# Close the connection to the database
engine.dispose()