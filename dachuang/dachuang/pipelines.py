# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class MongoPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        # self.client.dachuang.fupin.insert(item)
        self.client.dachuang.douban.insert(item)
        return item

    def close_spider(self,spider):
        self.client.close()
