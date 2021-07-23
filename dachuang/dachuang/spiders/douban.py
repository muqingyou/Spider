import time

import requests
import scrapy
import pymongo
from lxml import etree
from selenium import webdriver
# import time
# from selenium.webdriver import ChromeOptions
client = pymongo.MongoClient('localhost', 27017)
db = client['dachuang']
table = db['fupin']
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']


    def parse(self, response):
        # 连接数据库

        result = table.find({}, {'_id': 0, 'date': 0})
        url = "https://www.douban.com/search?cat="
        #url = "https://www.douban.com/search?q="

        count = 0
        # for a in result:
        #     yield scrapy.Request(url+a['title'], callback=self.parse_search)
        #     count += 1
        #     if count > 5:
        #         break
        for a in result:
            # # #日记 https://www.douban.com/search?cat=1015&q=%E6%89%B6%E8%B4%AB
            # # yield scrapy.Request(url+'1015&q='+a['title'], callback=self.parse_note_search)
            # #小组
            # yield scrapy.Request(url+'1019&q='+a['title'], callback=self.parse_group_search)
            if a['title'] is not None:
                yield scrapy.Request(url + '1015&q=' + a['title'], callback=self.parse_search, meta={"keyword": a['title']})


            #yield scrapy.Request(url + '1019&q=' + a['title'], callback=self.parse_search)

            # count += 1
            # if count > 0:
            #     break
    def parse_search(self,response):
        urls = response.xpath('//div[@class="title"]//a/@href').extract()
        if len(urls) == 0:
            pass  # 没内容
        else:
            #if response.url.find('1015')!=-1:
            for url in urls:
                yield scrapy.Request(url, callback=self.parse_note, meta={"keyword":response.meta['keyword'],"comments":[]})
            # else:
            #     for url in urls:
            #         yield scrapy.Request(url, callback=self.parse_group, meta={"comments": []})

    # def parse_note_search(self,response):
    #     urls = response.xpath('//div[@class="title"]//a/@href').extract()
    #     if len(urls) == 0:
    #         pass #没内容
    #     else:
    #         for url in urls:
    #             yield scrapy.Request(url, callback=self.parse_note,meta={"comments":[]})
    #
    # def parse_group_search(self,response):
    #     urls = response.xpath('//div[@class="title"]//a/@href').extract()
    #     if len(urls) == 0:
    #         pass  # 没内容
    #     else:
    #         for url in urls:
    #             yield scrapy.Request(url, callback=self.parse_group, meta={"comments": []})

    # def parse_search(self,response):
    #     #展开更多page_source
    #     driver = webdriver.Chrome(executable_path='D:\pycharm-file\chromedriver_win32\chromedriver.exe')  # 创建Chrome对象.
    #     # 操作这个对象.
    #     driver.get(response.url)
    #     time.sleep(2)
    #     webElement = driver.find_element_by_xpath("//div[@class='result-list-ft']")
    #     webElement.click()



    #     results = response.xpath("//div[@class='result-list']/div[@class='result']")
    #     for result in results:
    #         #详情url
    #         url = result.xpath(".//div[@class='title']//h3//a//@href").extract_first()
    #         if url.find('group') != -1:
    #             yield scrapy.Request(url, callback=self.parse_group)
    #         # elif url.find('note') != -1:
    #         #     yield scrapy.Request(url, callback=self.parse_note,meta={"comments":[]})
    #     #driver.quit()

    def parse_group(self,response):
        print("小组")

    def parse_note(self,response):
        #if response.xpath("/html/body/div[@class='account-body login-wrap login-start']").extract()!=[]:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(executable_path='D:\pycharm-file\chromedriver_win32\chromedriver.exe',chrome_options=option)
        # 网站登陆页面
        browser.get(response.url)
        handle = browser.current_window_handle
        # 等待3s用于加载脚本文件
        browser.implicitly_wait(3)
        browser.find_element_by_class_name('ui-overlay-close').click()
        time.sleep(1)
        source = browser.page_source
        html = etree.HTML(source)

        #评论（本来就可以无评论）
        comments = []
        # #无评论
        # if len(html.xpath("//div[@class='comment-content']//text()")) == 0:
        #     pass
        # else:
        # #有评论
        timeList = html.xpath("//time//text()")
        contentList = html.xpath("//div[@class='comment-content']//text()")
        comments.extend(response.meta['comments'])
        for i in range(len(timeList)):
            comment = {
                'time': timeList[i],
                'content':contentList[i]
            }
            comments.append(comment)
        #多页评论
        if len(html.xpath('//a[@class="next"]//text()'))!=0:
            print("".join(html.xpath('//a[@class="next"]/@href')))
            yield scrapy.Request("".join(html.xpath('//a[@class="next"]/@href')), callback=self.parse_note,meta={"keyword":response.meta['keyword'],"comments":comments})
        else:
            title = html.xpath("//h1//text()")
            title = "".join(title)
            date = html.xpath('//span[@class="pub-date"]//text()')
            date = "".join(date)
            passage = html.xpath('//div[@class="note"]//text()')
            passage = "".join(passage)
            yield {
                'title':title,
                'date':date,
                'passage':passage,
                'comments':comments,
                "keyword": response.meta['keyword'],
            }
            table.delete_many({"title": response.meta['keyword']})
        browser.quit()


