import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for _ in response.css('div.quote'):

            yield {
                'quote': _.css('span.text::text').get(),
                'author': _.css('small.author::text').get(),
                'tags': _.css('div.tags a.tag::text').getall()
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)