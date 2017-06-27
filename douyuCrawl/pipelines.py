# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from douyuCrawl.settings import IMAGES_STORE

class DouyucrawlPipeline(ImagesPipeline):

	# 重构get_media_requests方法
    def get_media_requests(self, item, info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    # 重构item_completed方法，对下载的图片进行重命名（以主播昵称作为头像名称）
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(IMAGES_STORE + image_path[0], IMAGES_STORE + item['nickname'] + ".jpg")
        return item
