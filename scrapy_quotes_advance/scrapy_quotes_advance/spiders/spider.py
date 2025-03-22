import scrapy

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/random"]
    
    def parse(self, response):
        for _ in response.css('div.quote'):

            yield {
                'quote': _.css('span.text::text').get(),
                'author': _.css('span > small.author::text').get(),
                'tags': _.css('div.tags > a.tag::text').getall()
            }