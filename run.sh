#!/bin/bash
git clone https://github.com/rangertaha/scrapy-prometheus-exporter && \
    cd scrapy-prometheus-exporter/ && \
    pip install . && \
    cd ../ && \
    scrapy crawl HttpbinSpider
