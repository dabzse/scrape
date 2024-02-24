import scrapy
from ..items import ScrapeItem

class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        items = ScrapeItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
