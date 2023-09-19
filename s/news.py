import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
# data={'name':'jinbeom'}
# headers={'Content-Type':'application/json; charset=utf-8'}
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select('tr'>'td')
print(result)
print(result.text)