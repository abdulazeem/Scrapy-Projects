# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys

class SilkySpider(scrapy.Spider):
    name = 'silky'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=20,
            screenshot=True,
            callback=self.parse
        )


    def parse(self, response):
        # img=response.meta['screenshot']

        # with open('screen.png','wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_form_input_homepage']")
        search_input.send_keys('Hello Workd')

        search_input.send_keys(Keys.ENTER)

        driver.save_screenshot('enter.png')

        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath("//div[@class='result__extras__url']/a")

        for link in links:
            yield {
                'URL':link.xpath(".//@href").get()
            }


        driver.close()
        



