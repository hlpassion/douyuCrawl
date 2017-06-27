# -*- coding: utf-8 -*-
import scrapy
from douyuCrawl.items import DouyucrawlItem
import json


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]

    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.text)['data']
        if len(data_list) == 0:
            return

        for data in data_list:
            item = DouyucrawlItem()
            item['nickname'] = data['nickname']
            item['imagelink'] = data['vertical_src']
            yield item

        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)
