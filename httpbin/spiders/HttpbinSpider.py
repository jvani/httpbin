# -*- coding: utf-8 -*-
import json
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'HttpbinSpider'
    allowed_domains = ['httpbin.org']

    def start_requests(self):
        self.request = scrapy.Request(
            'http://httpbin.org/post',
            method='POST',
            body=b'hello world',
            callback=self.parse
        )
        yield self.request

    def parse(self, response):
        data = json.loads(response.body.decode())
        self.logger.info(json.dumps(data, indent=4))
        # -- Loop infinitely.
        yield self.request
