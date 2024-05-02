This repository is a crawler to obtain the history of financial trading markets OHLC (open, high, lose, close) data and real-time price by the crawler framework scrapy, and stores it in the database. This project currently only accesses coinmarketcap's API and stores it in mongoDB. In the future work, other source APIs and stored databases will be added.

## Installation

```bash
git clone https://github.com/mashiro7916/MarketCrawler.git
pip install -r requirements.txt
```
## Set mongoDB 
Set mongoDB named finance(you can change it in [setting.py](MarketCrawler/MarketCrawler/setting.py))
## Start crawl
```bash
python start_history_crawler.py
```
