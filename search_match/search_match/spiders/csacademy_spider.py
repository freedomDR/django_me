# coding=utf-8

import scrapy
from scrapy.spiders import CrawlSpider
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from scrapy.utils.project import get_project_settings
from scrapy import signals
from pydispatch import dispatcher
from bs4 import BeautifulSoup

from ..items import MatchInformationItem
from datetime import datetime
from ..decorator import clean_match


class CsacademySpider(CrawlSpider):
    name = 'csacademy_spider'
    start_urls = ['https://csacademy.com/contests']
    # start_urls = ['https://blog.csdn.net/zwq912318834/article/details/79773870']

    @clean_match('csacademy')
    def __init__(self):
        self.mySetting = get_project_settings()

        self.timeout = self.mySetting['SELENIUM_TIMEOUT']
        self.isLoadImage = self.mySetting['LOAD_IMAGE']
        self.windowHeight = self.mySetting['WINDOW_HEIGHT']
        self.windowWidth = self.mySetting['WINDOW_WIDTH']
        opt = webdriver.FirefoxOptions()
        opt.headless = True
        self.browser = webdriver.Firefox(firefox_options=opt)
        if self.windowHeight and self.windowWidth:
            self.browser.set_window_size(self.windowWidth, self.windowHeight)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, 60, 1)
        super(CsacademySpider, self).__init__()
        dispatcher.connect(receiver=self.csacademy_spider_close_handle, signal=signals.spider_closed)

    def csacademy_spider_close_handle(self, spider):
        logging.info('firefox quit')
        self.browser.quit()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,
                                 meta={'usedSelenium': True})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        logging.info(soup.table)
        tmp = soup.table.find_all('tr')[1:]
        logging.info('time %s', soup.table.find_all('tr'))
        for line in tmp:
            data = MatchInformationItem()
            data['match_website'] = 'https://csacademy.com/contests'
            logging.info(str(line.find_all('td')[1].text))
            time_tmp = line.find_all('td')[1].text.split('local')[0].strip()
            time_tmp = datetime.strptime(time_tmp, '%d/%m/%Y, %H:%M')
            data['match_start_date'] = time_tmp.strftime('%Y-%m-%d %X')
            data['match_name'] = line.a.text
            data['match_time_length'] = line.find_all('td')[2].text
            data['match_writer'] = 'null'
            data['match_register'] = 'no'
            data['match_before_start'] = 'null'
            yield data
        pass

