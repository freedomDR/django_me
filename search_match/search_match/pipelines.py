# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import MatchInformationItem, TestItem
from django.core.exceptions import ObjectDoesNotExist
import logging


class SearchMatchPipeline(object):
    def process_item(self, item, spider):
        # item.save()
        # print(item)
        logging.warning('start deal pipeline')
        if isinstance(item, TestItem):
            pass
        elif isinstance(item, MatchInformationItem):
            try:
                logging.info(item['match_name'])
                MatchInformationItem.django_model.objects.get(match_name=item['match_name'],
                                                              match_website=item['match_website'])
            except ObjectDoesNotExist:
                item.save()
                return item
        else:
            return None


# class MatchInformationPipeline(object):
#     def process_item(self, item, spider):
#         item = MatchInformationItem()
#         return item

