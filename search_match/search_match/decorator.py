# -*- coding: utf-8 -*-
from functools import wraps
import logging
from .items import MatchInformationItem
import wrapt


def clean_match(name):
    @wrapt.decorator
    def clean(wrapped, instance, args, kwargs):
        logging.info('{} 开始删除比赛装饰器'.format(instance.name))
        delete_match = set()
        tmp = MatchInformationItem.django_model.objects.all()
        for data in tmp:
            logging.info('match_name {0}'.format(data.match_name))
            if data.match_website.find(name) != -1:
                delete_match.add(data.match_name)
                data.delete()
        if delete_match:
            logging.warning('delete {} match: {}'.format(name, delete_match))
        logging.info('结束删除比赛装饰器')
        wrapped()
    return clean
#def clean_match(name):
#    def decorate(func):
#        def clean(*args, **kwargs):
#            print('{} 开始删除比赛装饰器'.format(func.__name__))
#            delete_match = set()
#            tmp = MatchInformationItem.django_model.objects.all()
#            for data in tmp:
#                logging.info('match_name {0}'.format(data.match_name))
#                if data.match_website.find(name) != -1:
#                    delete_match.add(data.match_name)
#                    data.delete()
#            if delete_match:
#                logging.warning('delete {} match: {}'.format(name, delete_match))
#            print('结束删除比赛装饰器')
#            func()
#        return clean
#    return decorate
