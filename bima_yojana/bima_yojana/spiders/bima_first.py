# -*- coding: utf-8 -*-
import scrapy


class BimaFirstSpider(scrapy.Spider):
    name = 'bima_first'
    allowed_domains = ['https://pmfby.gov.in/ceo/dashboard']
    start_urls = ['http://https://pmfby.gov.in/ceo/dashboard/']

    def parse(self, response):
        pass
