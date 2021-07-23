import scrapy


class ProxydemoSpider(scrapy.Spider):
    name = 'proxydemo'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def start_requests(self):
        while True:
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse,dont_filter=True)

    def parse(self, response):
        print(response.text)
