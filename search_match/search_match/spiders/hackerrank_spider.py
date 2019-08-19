# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from ..items import MatchInformationItem
from ..decorator import clean_match
from datetime import datetime
import logging


class HackerrankSpiderSpider(CrawlSpider):
    name = 'hackerrank_spider'
    allowed_domains = ['www.hackerrank.com']
    start_urls = ['http://www.hackerrank.com/contests']

    @clean_match('hackerrank')
    def __init__(self):
        super(HackerrankSpiderSpider, self).__init__()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        active_contests = soup.find('div', class_='active_contests')
        if active_contests:
            for line in active_contests.find_all('li')[1:]:
                data = MatchInformationItem()
                data['match_name'] = line.find_all('div', class_='contest-name')[0].text
                tmp_start_time = line.find_all('meta')[0]['content']
                tmp_start_time = datetime.strptime(tmp_start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                data['match_start_date'] =tmp_start_time.strftime('%Y-%m-%d %X')
                data['match_time_length'] = line.find_all('meta')[2]['content'].replace('PT','')
                data['match_writer'] = 'null'
                data['match_register'] = 'no'
                data['match_before_start'] = 'null'
                data['match_website'] = 'https://www.hackerrank.com/contests'
                yield data
            pass
        pass
