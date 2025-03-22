import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        for _ in response.css('ol.row > li'):

            rating = _.css('p.star-rating::attr(class)').get()
            cleaned_rating = rating.replace('star-rating ', '')

            yield {
                "title": _.css('a::attr("title")').get(),
                "rating": cleaned_rating,
                "price": _.css('div.product_price p.price_color::text').get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)