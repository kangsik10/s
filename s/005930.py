import requests
from bs4 import BeautifulSoup
key = input("회사명을 입력하시오 : ")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={key}")

html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)
