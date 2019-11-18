# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..decorator import clean_match
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from ..items import MatchInformationItem
from datetime import datetime
import ipdb
import logging

class CometojSpider(scrapy.Spider):
    name = 'cometoj_spider'
    start_urls = ['https://cometoj.com/contests/']

    @clean_match('cometoj')
    def __init__(self):
        self.mySetting = get_project_settings()
        self.timeout = self.mySetting['SELENIUM_TIMEOUT']
        opt = webdriver.FirefoxOptions()
        opt.headless = True
        self.browser = webdriver.Firefox(firefox_options=opt)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, 60, 1)
        super(CometojSpider, self).__init__()
        dispatcher.connect(receiver=self.cometoj_spider_close_handle, signal=signals.spider_closed)

    def cometoj_spider_close_handle(self, spider):
        self.browser.quit()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={'usedSelenium':True, 'element_xpath':"/html/body/div[1]/div[2]/div/div[2]/div[2]/div"})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        contests = soup.find('div', class_='contest-list-row').find('div', class_='ivu-card-body').find('div', class_='panel-body').find_all('li',class_="contests-item")
        for contest in contests:
            data = MatchInformationItem()
            curtime = datetime.today()
            # judge is first
            if('top' in contest.attrs.get('class')):
                data['match_name'] = contest.find('p',class_='title').text
                tmp = contest.find('p',class_='time').find_all('span')
                start_time = datetime.strptime(tmp[0].text[5:].strip(), '%Y-%m-%d %H:%M')
                if(curtime > start_time):
                    continue
                data['match_start_date'] = start_time.strftime('%Y-%m-%d %X')
                data['match_time_length'] = tmp[1].text[5:].strip()
                data['match_register'] = tmp[2].text[5:].strip()
            else:
                data['match_name'] = contest.find('p',class_='title').text
                tmp = contest.find('ul',class_='detail').find_all('li')
                start_time = datetime.strptime(tmp[0].text.strip(), '%Y-%m-%d %H:%M')
                if(curtime > start_time):
                    continue
                data['match_start_date'] = start_time.strftime('%Y-%m-%d %X')
                data['match_time_length'] = tmp[1].text.strip()
                data['match_register'] = tmp[2].text.strip()
                pass
            data['match_writer'] = 'null'
            data['match_before_start'] = 'null'
            data['match_website'] = 'https://cometoj.com/contests'
            yield data
