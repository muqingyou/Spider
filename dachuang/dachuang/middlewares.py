# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#
from importlib import reload

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# import matplotlib.pylab as plt
import sys
import json
import chardet
import time

# class SeleniumMiddlewares(object):
#     def __init__(self):
#         self.chrome_opt = webdriver.ChromeOptions()
#         prefs = {
#             "profile.managed_default_content_settings.images": 2,
#             "plugins.plugins_disabled": ['Chrome PDF Viewer'],
#             "plugins.plugins_disabled": ['Adobe Flash Player'],
#                  }
#         self.chrome_opt.add_experimental_option("prefs", prefs)
#     def process_request(self, request, spider):
#         login_url='https://passport.weibo.cn/signin/login'
#         #如果request是login_url
#         if request.url==login_url:
#             self.driver = webdriver.Chrome(executable_path='D:\pycharm-file\chromedriver_win32\chromedriver.exe', options=self.chrome_opt)
#         self.driver.implicitly_wait(5)# 延迟，为了加载元素，否则照顾到元素，出现异常
#         input_name = self.driver.find_element(By.ID, 'loginName')
#         input_name.clear()  # 清楚文本框中的内容
#         input_name.send_keys('15608190701')  # 输入账号
#         input_pass = self.driver.find_element(By.ID, 'loginPassword')
#         input_pass.clear()
#         input_pass.send_keys('7204242qingyou')  # 输入密码
#         time.sleep(5)
#         self.driver.find_element(By.ID, 'loginAction').click()
#         print(self.driver.page_source)  # 查看源代码


import random

#from settings import IPPOOL


# class ProxychiMiddleware(object):
#
#     IPPOOL = [
#         {"ipaddr":"124.158.175.2:8080"},
#         {"ipaddr":"218.88.204.207:3256"},
#         {"ipaddr":"182.122.146.78:9999"},
#         {"ipaddr":"113.128.123.246:9999"},
#         {"ipaddr":"223.243.174.228:9999"},
#     ]
#
#     # 定义一个请求之前的方法
#     def process_request(self, request, spider):
#         # 如果是 私密代理
#         # request.meta['proxy'] = 'https://用户名and密码114.212.12.4:3128'
#         # 随即获取一个代理
#         this_ip = random.choice(self.IPPOOL)
#         request.meta['proxy'] = 'HTTP://' + this_ip["ipaddr"]
#         return None
from scrapy import signals
from w3lib.http import basic_auth_header
class ProxyDownloaderMiddleware:

    def process_request(self, request, spider):
        proxy = "tps133.kdlapi.com:15818"
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': proxy}
        # 用户名密码认证
        request.headers['Proxy-Authorization'] = basic_auth_header('t12383775821861', 'l59ourft')  # 白名单认证可注释此行
        request.headers["Connection"] = "close"
        return None



# from scrapy import signals
#
# # useful for handling different item types with a single interface
# from itemadapter import is_item, ItemAdapter
#
#
# class DachuangSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class DachuangDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
# from scrapy.http import HtmlResponse
# from logging import getLogger
#
#
# class SeleniumMiddleware():
#     def __init__(self, timeout=None, weibo_username=None, weibo_password=None):
#         self.logger = getLogger(__name__)
#         self.timeout = timeout
#         self.weibo_username = 751535624@qq.com
#         self.weibo_password = 7204242qingyou
#         self.chrome_options = Options()
#         self.chrome_options.add_argument('--headless')
#         self.chrome_options.add_argument('--disable-gpu')
#         self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
#         self.browser.set_page_load_timeout(self.timeout)
#         self.wait = WebDriverWait(self.browser, self.timeout)
#
#         # 淘宝登录
#         self.browser.get(
#             'http://s.weibo.com/weibo')
#         # 切换到登录
#         login = self.wait.until(EC.element_to_be_clickable((By.XPATH, '''//a[@node-type='loginBtn']''')))
#         login.click()
#         # 输入微博用户名
#         username_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
#         username_input.send_keys(self.weibo_username)
#         # 输入微博密码
#         password_input = self.browser.find_element_by_name('password')
#         password_input.send_keys(self.weibo_password)
#         # 提交
#         weibo_submit = self.browser.find_element_by_class_name('W_btn_a btn_34px')
#         weibo_submit.send_keys(Keys.ENTER)
#
#     def __del__(self):
#         self.browser.close()
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
#                    weibo_username=crawler.settings.get('WEIBO_USERNAME'),
#                    weibo_password=crawler.settings.get('WEIBO_PASSWORD'))
#
#     def process_request(self, request, spider):
#         '''
#         用PhantomJS抓取页面
#         :param request: Request对象
#         :param spider: Spider对象
#         :return: HtmlResponse
#         '''
#         self.logger.debug('Chrome headless is Starting')
#         page = request.meta.get('page', 1)
#         try:
#             # 不是第一页，跳转翻页
#             if page > 1:
#                 # 跳转页面输入框
#                 input = self.wait.until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
#                 # 跳转确定
#                 submit = self.wait.until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
#                 input.clear()
#                 # 输入需要跳转的页面
#                 input.send_keys(page)
#                 submit.click()
#             # 等待页面跳转
#             self.wait.until(
#                 EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
#             # 下拉界面到最下方
#             self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#             # 等待商品页面加载完毕
#             self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
#             return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
#                                 status=200)
#         except TimeoutException:
#             return HtmlResponse(url=request.url, request=request, status=500)
