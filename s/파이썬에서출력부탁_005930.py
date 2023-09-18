import FinanceDataReader as fdr
import pandas as pd
df_krx=fdr.StockListing('KRX')
df=fdr.DataReader("005930","2023-08-01","2023-08-31")
df.to_csv("stock.csv")