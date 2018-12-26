import scrapy
import logging
from ..items import MatchInformationItem
from datetime import datetime
from ..decorator import clean_match


class CodeforcesSpider(scrapy.Spider):
    name = 'codeforces_spider'

    # start_urls=['http://www.codeforces.com/contests']

    @clean_match('codeforces')
    def __init__(self):
        super(CodeforcesSpider, self).__init__()

    def start_requests(self):
        urls = ['http://www.codeforces.com/contests']
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        tmp = response.css('html body #body div #pageContent div.contestList div.datatable div table')[0]
        tmp = tmp.css('tr')[1:]
        for line in tmp:
            data = MatchInformationItem()
            data['match_website']='http://www.codeforces.com/contests'
            data['match_name']=str(line.css('td')[0].css('td::text').extract_first().strip())
            data['match_writer']=line.css('td')[1].css('td::text').extract_first().strip()
            time_tmp = line.css('td')[2].css('td span::text').extract_first().strip()
            time_tmp = datetime.strptime(time_tmp, '%b/%d/%Y %H:%M')
            data['match_start_date']= time_tmp.strftime('%Y-%m-%d %X')
            data['match_time_length']=line.css('td')[3].css('td::text').extract_first().strip()
            data['match_before_start']=line.css('td')[4].css('td span::text').extract_first().strip()
            # data#'register': line.css('td a::text')[5].extract().strip()
            if line.css('td')[5].css('a') == []:
                data['match_register'] = 'no'
            else:
                data['match_register'] = str(line.css('td')[5].css('td a::text')[1].extract()).strip()
            yield data
            # item = TestItem()
            # item['test_name'] = 'shabi'
            # yield item

    # def parse(self, response):
    #     item = MatchInformationItem()
    #     item['match_writer'] = 'dr'
    #     return item

    def __call__(self, *args, **kwargs):
        self.__init__()