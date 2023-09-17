import FinanceDataReader as fdr
import pandas as pd
df_krx=fdr.StockListing('KRX')
df=fdr.DataReader("005930","2023-08-01","2023-08-31")
df

# import FinanceDataReader as fdr
# import pandas as pd
# df_krx = fdr.StockListing('KRX')
# df_krx

# install -U finance-datareader
# import FinanceDataReader as fdr
# import pandas as pd
# df_krx =fdr.StockListing('KRX').iloc[:, :3]
# stocks = ["005930"]
# df1 = pd.DataFrame()
# for i in stocks:
#     df = dfr.DataReader(i, '2023-08-01','2023-08-31')
#     df["Symbol"] = i
#     df1 = pd.concat([df1, df])
# df1.reset_index().merge(df_krx, how="left")

# import requests
# from bs4 import BeautifulSoup
# key = input("회사명을 입력하시오 : ")
# response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={key}")

# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select(".news_tit")
# for link in links:
#     title = link.text
#     url = link.attrs['href']
#     print(title, url)
