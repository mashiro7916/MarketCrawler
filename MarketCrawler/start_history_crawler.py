from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import cryptocurrency_cfg
import time
import argparse


def start_crawler(spider, params):
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider, params)
    process.start()
    # process.stop()
    # process.join()
    return process


def to_second(interval):
    alpha = interval[len(interval) - 1]
    if alpha.__eq__('h'):
        return int(interval[0:len(interval) - 1]) * 60 * 60
    elif alpha.__eq__('d'):
        return int(interval[0:len(interval) - 1]) * 60 * 60 * 24


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--iter', help='Set data interval', default='1h', choices=['1h', '1d', '7d', '30d'])
    parser.add_argument('--itercrawl', help='Set the amount of data to crawl each time', default='1d')
    parser.add_argument('--times', help='Set how many times to crawl', default='10', type=int)
    args = parser.parse_args()
    time_list = [int(time.time()) - to_second(args.itercrawl) * i for i in range(args.times)][::-1]
    request_list = []
    for cryptocurrency in cryptocurrency_cfg.cryptocurrency_list:
        for time in time_list:
            request_list.append({"id": cryptocurrency['id'], "convertId": 2781, "timeStart": time - to_second(args.itercrawl), "timeEnd": time,
                                 "interval": args.iter})
    start_crawler("crypto_spider",request_list)

