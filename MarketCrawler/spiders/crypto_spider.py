import scrapy
from scrapy.http import Request
import json
from urllib.parse import urlencode
from MarketCrawler.items import CryptoCurrency
from scrapy.loader import ItemLoader

class CryptoSpider(scrapy.Spider):
    name = "crypto_spider"
    allowed_domains = ['api.coinmarketcap.com']

    def __init__(self, *args, **kwargs):
        super(CryptoSpider, self).__init__(*args, **kwargs)
        self.url = 'https://api.coinmarketcap.com/data-api/v3.1/cryptocurrency/historical?'
        self.request_list = args
        self.name = "crypto_spider"

    def start_requests(self):
        print("start_requests")
        for request in self.request_list[0]:
            url = self.url + urlencode(request)
            print(url)
            yield Request(url, self.parse)

    def parse(self, response, **kwargs):
        response = json.loads(response.body)
        idx = response['data']['id']
        symbol = response['data']['symbol']
        results = response['data']['quotes']
        for result in results:
            quote = result['quote']
            yield CryptoCurrency(
                id=idx,
                symbol=symbol,
                datetime=result['timeOpen'],
                # datetime_close=result['timeClose'],
                open=quote['open'],
                high=quote['high'],
                low=quote['low'],
                close=quote['close'],
                volume=quote['volume']
                # marketCap=quote['marketCap'],
            )

