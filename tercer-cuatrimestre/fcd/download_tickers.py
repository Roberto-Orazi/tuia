import yfinance as yf
import pandas as pd

# Lista de tickers de acciones argentinas
tickers = ["YPF", "PAM", "BMA", "BBAR", "GGAL", "CEPU"]

# Crear DataFrame vacío
df = pd.DataFrame()

# Descargar los datos de cada ticker
for ticker in tickers:
    data = yf.download(ticker, start="2020-01-01", end="2024-10-01")

    # Añadir columna con el nombre del ticker
    data["Ticker"] = ticker

    # Calcular la variación diaria del precio
    data["Price Variation"] = data["Adj Close"].pct_change()

    # Añadir columna con el sector (esto es manual, depende de los datos que encuentres)
    data["Sector"] = "Sector correspondiente"  # Ej. "Energía", "Finanzas"

    # Añadir columna con país
    data["País"] = "Argentina"

    # Concatenar los datos al DataFrame principal
    df = pd.concat([df, data])

# Limpiar datos faltantes
df.dropna(inplace=True)

# Guardar el dataset transformado
df.to_csv("acciones_argentinas.csv", index=True)
