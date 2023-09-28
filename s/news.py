# from docx import Document

# # 1. 워드 생성하기
# document = Document()

# # 2. 워드 데이터 추가하기
# document.add_heading('기사 제목', level=0)
# document.add_paragraph('기사 링크')
# document.add_paragraph('기사 본문')

# # 3. 워드 저장하기
# document.save("test.docx")
# # [출처] 크롤링 - 파이썬으로 워드문서 다루기 python-docx <삼성전자 뉴스 1개 넣어보기>|작성자 카페인노예



from docx import Document
import requests
from bs4 import BeautifulSoup

# 1. 워드 생성하기
document = Document()

response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&oquery=%7Bkeyword%7D&tqi=iaKNxsp0J14ssAv%2B2dhssssss3o-193342")
html = response.text
soup = BeautifulSoup(html,'html.parser')
articles = soup.select("div.info_group")
links = articles[0].select("a.info")
url = links[1].attrs['href']
response = requests.get(url , headers={'User-agent':'Mozila/5.0'})
html = response.text
soup = BeautifulSoup(html , 'html.parser')
title = soup.select_one('#title_area').text
content = soup.select_one("#dic_area")
본문 = content.text


# 2. 워드 데이터 추가하기
document.add_heading(title, level=0)
document.add_paragraph(url)
document.add_paragraph(본문)

# 3. 워드 저장하기
document.save("news.docx")
# [출처] 크롤링 - 파이썬으로 워드문서 다루기 python-docx <삼성전자 뉴스 1개 넣어보기>|작성자 카페인노예