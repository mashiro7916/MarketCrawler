# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from datetime import datetime
from MarketCrawler import settings
from scrapy.exceptions import DropItem
import logging


class MarketcrawlerPipeline:
    collection_name = "cryptocurrency"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):

        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB", "items"),
        )

    def open_spider(self, spider):
        self.items = []
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        formatted_datetime = datetime.strptime(item['datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        newdict = {"metadata": {
            "symbol": item['symbol'],
            "source": "coinmarketcap"
        }, 'timestamp': formatted_datetime, 'open': item['open'], 'close': item['close'],'volume':item['volume']}
        self.db[self.collection_name].insert_one(newdict)


        return item
