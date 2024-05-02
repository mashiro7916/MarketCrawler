This repository is a crawler to obtain the history of financial trading markets OHLC (open, high, lose, close) data and real-time price by the crawler framework scrapy, and stores it in the database. This project currently only accesses coinmarketcap's API and stores it in mongoDB. In the future works, other source APIs and stored databases will be added.

## Installation

```bash
git clone https://github.com/mashiro7916/MarketCrawler.git
pip install -r requirements.txt
```
## Set mongoDB 
Set mongoDB database named finance(you can change it in [settings.py](MarketCrawler/settings.py)) and set collection named cryptocurrency(you can change it in [pipelines.py](MarketCrawler/pipelines.py)).Then in this repository,set the collection be time series data,so needed a timestamp key for record datetime.
## Start crawl
```bash
python start_history_crawler.py
```

## Feature works
More source:\n
This repository currently only obtains hourly cryptocurrency history OHLC data from coinmarketcap,the goal is to obtain minute-by-minute data that extends beyond the OHLC data,and get data from more sources such as Binance API.

Real time quotes:
In order for a trading bot to operate, it needs to have access to real-time and accurate data.

More repository databases:
There are two types of databases, RDBMS and NoSQL. This repository currently only stores data in mongoDB which is NoSQL database. Hope it can also be stored in RDBMS, that currently considering using postgresql.

