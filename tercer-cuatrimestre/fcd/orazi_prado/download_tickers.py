import yfinance as yf
import pandas as pd

final_df = pd.DataFrame()

# Lista de tickers
bank_tickers = [
    "HSBC",  # HSBC Holdings plc (Reino Unido)
    "BBVA",  # Banco Bilbao Vizcaya Argentaria, S.A. (España)
    "SAN",  # Banco Santander, S.A. (España)
    "BNS",  # Bank of Nova Scotia (Canadá)
    "TD",  # Toronto-Dominion Bank (Canadá)
    "DB",  # Deutsche Bank AG (Alemania)
    "UBS",  # UBS Group AG (Suiza)
    "ITUB",  # Itaú Unibanco Holding S.A. (Brasil)
    "BBAS3.SA",  # Banco do Brasil S.A. (Brasil)
    "WBC.AX",  # Westpac Banking Corporation (Australia)
    "ANZ.AX",  # Australia and New Zealand Banking Group Limited (Australia)
    "ICICIBANK.NS",  # ICICI Bank Limited (India)
    "HDFCBANK.NS",  # HDFC Bank Limited (India)
    "KB",  # KB Financial Group Inc. (Corea del Sur)
    "SMFG",  # Sumitomo Mitsui Financial Group, Inc. (Japón)
    "GGAL",  # Grupo Financiero Galicia S.A. (Argentina)
]


for ticker in bank_tickers:
    # Descargar datos del ticker
    stock = yf.Ticker(ticker)

    historic = stock.history(period="1y")

    if not historic.empty:
        # Obtener información adicional
        information = stock.info

        temp_df = pd.DataFrame(
            {
                "Date": historic.index,  # Variable Temporal
                "Ticker": [ticker] * len(historic),  # Variable Categórica
                "Open": historic["Open"],  # Variable Numérica Continua
                "High": historic["High"],  # Variable Numérica Continua
                "Low": historic["Low"],  # Variable Numérica Continua
                "Close": historic["Close"],  # Variable Numérica Continua
                "Volume": historic["Volume"],  # Variable Numérica Discreta
                "Market Cap": [information.get("marketCap", None)]
                * len(historic),  # Variable Numérica Discreta
                "Sector": [information.get("sector", "N/A")]
                * len(historic),  # Variable Categórica
                "City": [information.get("city", "N/A")]
                * len(historic),  # Variable Categórica/geografica
                "Country": [information.get("country", "N/A")]
                * len(historic),  # Variable Categórica/geografica
            }
        )

        final_df = pd.concat([final_df, temp_df], axis=0)

print(final_df.head())

if not final_df.empty:
    final_df.to_csv("bank_tickers_data.csv", index=False)
    print("Data save in 'bank_tickers_data.csv'")
else:
    print("No data available to save")
