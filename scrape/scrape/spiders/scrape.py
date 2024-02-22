import scrapy


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            yield {
                'title': title,
                'author': author,
                'tags': tag,
            }
