import scrapy

class SamsungNewsSpider(scrapy.Spider):
    name = 'samsung_news'
    allowed_domains = ['news.samsung.com']  # 크롤링 대상 도메인
    start_urls = ['https://news.samsung.com/']

    def parse(self, response):
        for article in response.css('.news-list-item'):
            title = article.css('.news-title a::text').get()
            link = article.css('.news-title a::attr(href)').get()
            date = article.css('.news-date::text').get()

            yield {
                'title': title,
                'link': link,
                'date': date,
            }

        next_page = response.css('.pagination .next-page a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

