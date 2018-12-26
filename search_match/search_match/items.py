# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import django
django.setup()
from scrapy_djangoitem import DjangoItem
from info.models import MatchInformation, Test

# class SearchMatchItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class MatchInformationItem(DjangoItem):
    django_model = MatchInformation


class TestItem(DjangoItem):
    django_model = Test
