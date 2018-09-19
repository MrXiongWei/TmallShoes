# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TmallshoesSpider(scrapy.Spider):
    name = 'tmallshoes'
    allowed_domains = ['www.tmall.com']
    start_urls = ['https://www.tmall.com/']

    def __init__(self):
        '''
         option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.browser = webdriver.Chrome(executable_path=r"C:\ProgramData\Anaconda3\Library\bin\chromedriver.exe",
                                        option=option)
        '''
        self.browser = webdriver.Chrome(r'C:/ProgramData/Anaconda3/Library/bin/chromedriver.exe')
        self.wait = WebDriverWait(self.browser, 10)
        super(TmallshoesSpider, self).__init__()
        # dispatcher.connect(self.spider_closed, signals.spider_closed)  # 第二个参数是信号（spider_closed:爬虫关闭信号，信号量有很多）,第一个参数是当执行第二个参数信号时候要执行的方法

    def spider_closed(self, spider):
        # 当爬虫退出的时候关闭chrome
        print('spider closed')
        self.browser.quit()

    def parse(self, response):
        products = response.xpath('//*[@id="J_ItemList"]//*[@class="product"]')
        for product in products:
            print(str(product))