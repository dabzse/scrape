import scrapy


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        title = response.css('title').extract()
        yield { 'title': title }