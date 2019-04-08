#!/bin/bash
git clone https://github.com/rangertaha/scrapy-prometheus-exporter && \
    cd scrapy-prometheus-exporter/ && \
    pip install scrapy . && \
    cd ../ && \
    scrapy crawl HttpbinSpider
