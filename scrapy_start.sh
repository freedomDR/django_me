#!/bin/bash
pwd
cd ./search_match/
scrapy crawl codeforces_spider
scrapy crawl csacademy_spider
scrapy crawl hackerrank_spider
cd ../
