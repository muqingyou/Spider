import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from scrapy_redis.spiders import RedisSpider

class FupinSpiderSpider(CrawlSpider):
    name = 'fupin_spider'
    allowed_domains = ['f.china.com.cn']
    start_urls = ['http://f.china.com.cn/']
    #redis_key = 'fupin:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        # 扶贫动态
        url = response.xpath('/html/body/div[1]/div[3]/div[2]/h2/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫故事
        url = response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 减灾救灾
        url = response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 国际合作
        url = response.xpath('/html/body/div[1]/div[4]/div[1]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 慈善公益
        url = response.xpath('/html/body/div[1]/div[4]/div[1]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫模式
        url = response.xpath('/html/body/div[1]/div[4]/div[2]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 贫困状况
        url = response.xpath('/html/body/div[1]/div[4]/div[2]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 政策解读
        url = response.xpath('/html/body/div[1]/div[4]/div[3]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 精准扶贫
        url = response.xpath('/html/body/div[1]/div[4]/div[3]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 视频
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[1]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 独家
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[1]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 新闻发布厅
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[2]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 访谈
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[2]/h2/span[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 图解
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫观点
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[2]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫开发条例
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[3]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 打赢脱贫攻坚战的决定
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[4]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # “十三五”
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[5]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 对口支援
        url = response.xpath('/html/body/div[1]/div[6]/div[2]/h1[6]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 救助热线
        url = response.xpath('/html/body/div[1]/div[9]/div[3]/h1/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 中央文件
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div[1]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 决策者说
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 主战场
        url = response.xpath('/html/body/div[1]/div[6]/div[1]/div[4]/h2/span[1]/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 军令状
        url = response.xpath('/html/body/div[1]/div[7]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫词条
        url = response.xpath('/html/body/div[1]/div[8]/div[1]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 扶贫问与答
        url = response.xpath('/html/body/div[1]/div[9]/div[1]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)
        # 学生资助政策
        url = response.xpath('/html/body/div[1]/div[9]/div[2]/h2/span/a/@href').extract_first()
        yield scrapy.Request(url, callback=self.parse_page_url)

    def parse_page_url(self, response):
        urls = response.xpath('//*[@id="autopage"]/center/a/@href').extract()
        urls.insert(0, response.url)
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_feature)

    def parse_feature(self, response):
        urls = response.xpath('/html/body/div[3]/div[1]/ul/li/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        # 标题
        title = response.xpath('//h1/text()').extract_first()
        # 时间
        date = response.xpath('/html/body/div[3]//h2/text()').extract_first()
        if type(date) == str:
            date = date.split("|")[0][5:]
        else:
            date = response.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
        # 关键词
        keys = response.xpath('//p[@class="kword"]/span/text()').extract_first()
        if type(keys) == str:
            pass
        else:
            keys = response.xpath('//*[@id="kw"]//text()').extract_first()
        yield {
            'title': title,
            'date': date,
            'keys': keys
        }


