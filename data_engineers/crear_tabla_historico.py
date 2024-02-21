from conexion_pg import  db_url
import pandas as pd
import yfinance as yf
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table

# Crear el motor de la base de datos
engine = create_engine(db_url)

# Crear el objeto metadata
metadata = MetaData()

# Obtener la tabla 'historico'
historico = Table('historico', metadata, autoload_with=engine)

lista_tickers = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'NFLX', 'TSLA', 'META', 'AMD', 'XOM', 'UBER', 'QCOM', 'COIN', 'KO', 'BAC', 'HD', 'PYPL', 'JPM', 'UNH', 'V']


start_ticker = '2018-01-01'
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
try:
  historico.to_sql(
      name='historico',
      con=engine,
      schema='public',
      if_exists='replace',   
      index=False
  )
except Exception as e:
    print("Error al conectar a la base de datos:", e)
finally:
    # Cierra la conexión
    engine.dispose()
    print("Conexión cerrada.")


# Close the connection to the database
engine.dispose()