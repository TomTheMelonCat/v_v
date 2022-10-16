import scrapy
from web_scraper.items import WebScraperItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Sreality_Spider(scrapy.Spider):
    name = 'sreality_scrape'

    def start_requests(self):
        base_url = 'https://www.sreality.cz/hledani/prodej/byty'
        urls = [base_url]

        for idx in range(int(500/20)-1): # int(500/20)-1
            urls.append(base_url + f'?strana={idx+2}')

        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10, wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'dir-property-list')))

    def parse(self, response):
        list_of_items = response.xpath('//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div')

        for u in list_of_items:
            item = WebScraperItem()
            item['img_url'] = u.xpath(f'preact/div/div/a[1]/img/@src').extract_first()
            item['title'] = u.xpath(f'div/div/span/span[1]/text()').extract()
            if any(item.values()) is False:
                continue 
            yield item