import scrapy


class WebScraperItem(scrapy.Item):
    title = scrapy.Field()
    img_url = scrapy.Field()

