# -*- coding: utf-8 -*-
import scrapy
import json

class PlaybooksSpider(scrapy.Spider):
    name = 'playbooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/plays.json?limit=12/']

    def parse(self, response):
        resp = json.loads(response.body)
        ebooks = resp.get('works')
    
        for ebook in ebooks:
            yield {
                'title': resp.get('title'),
                'subject':resp.get('subject') 
                }
