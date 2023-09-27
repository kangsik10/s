import requests
from bs4 import BeautifulSoup

def get_news(URL) :
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, "html.parser")

  title = soup.select_one("h2#title_area span").text #제목
  date = soup.select_one("span.media_end_head_info_datestamp_time")['data-date-time'] #기사작성일시
  media = soup.select_one("a.media_end_head_top_logo img")['title'] #매체명 (예.한국경제)
  content = soup.select_one("div#newsct_article").text.replace("\n","") #기사원문

  return (title, date, media, content, URL)