import requests
from bs4 import BeautifulSoup

page = 1
date = '20230911'
oid = '003'

while True:

    print('page', page)

    params = {
        'mode':'LPOD',
        'mid':'sec',
        'oid':'003',
        'date':date,
        'page':str(page)
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    res = requests.get('https://news.naver.com/main/list.naver', params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    now_page = int(soup.select_one('div.paging strong').text.strip())
    
    if page != now_page:
        break

    lists = soup.select('ul.type06_headline > li')
    
    for idx, list in enumerate(lists):
        url = list.select_one('a').attrs['href']
        res_content = requests.get(url, headers=headers)
        soup_content = BeautifulSoup(res_content.text, 'html.parser')
        
        title = ''
        content = ''

        if soup_content.select_one('h2#title_area') != None:
            print('일반기사')
            title = soup_content.select_one('h2#title_area').text.strip()
            content = soup_content.select_one('article#dic_area').text.replace('\n','').strip()
        elif soup_content.select_one('div.news_headline h4') != None:
            print('스포츠기사')
            title = soup_content.select_one('div.news_headline h4').text.strip()
            content = soup_content.select_one('div#newsEndContents').text.replace('\n','').strip()
        elif soup_content.select_one('h2.end_tit') != None:
            print('연예기사')
            title = soup_content.select_one('h2.end_tit').text.strip()
            content = soup_content.select_one('#articeBody').text.strip()
        else:
            print('오류')
            print(url)
            
        # print(title)
        # print(content)
        # print()

    page += 1

print('크롤링종료')