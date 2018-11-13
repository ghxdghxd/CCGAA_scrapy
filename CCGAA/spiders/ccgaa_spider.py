# -*- coding: utf-8 -*-
import scrapy
from CCGAA.items import CcgaaItem

class ccgaaSpiderSpider(scrapy.Spider):
    #爬虫的名字
    name = 'ccgaa_spider'
    #允许的域名
    allowed_domains = ['52.25.87.215']

    #入口url
    start_urls = ['http://52.25.87.215/CCGAA']
    # site.php?site = upper_aerodigestive_tract

    def parse(self, response):
        table_list = response.xpath("//select[@class='plain']//option[@class='plain']//text()").extract()
        # table_list = [x for x in table_list]
        for i in table_list:
            url = response.url + "site.php?site=" + str(i)
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        table_list = response.xpath(
            '//div[@id="Content Box Content"]//tr[@style="background-color: #D7DDDD; color: black; text-align: center; text-decoration: none; font-weight: bold; "]/parent::*/tr')
        # print(table_list)
        for t_item in table_list[1:]:
            table_item = CcgaaItem()
            table_item['cell_line'] = t_item.xpath(".//td[1]//text()").extract_first()
            table_item['primary_site'] = t_item.xpath(".//td[2]//text()").extract_first()
            table_item['atcc_annotation'] = t_item.xpath(".//td[3]//text()").extract_first()
            table_item['eigenstrat'] = t_item.xpath(".//td[4]//text()").extract_first()
            # print(table_item)
            yield table_item

        next_links = response.xpath("//section//table[3]//td[2]//a/@href").extract()

        if len(next_links) == 2:
            next_link = next_links[0]
            if next_link.endswith("=1"):
                next_link = False
        else:
            next_link = next_links[2]

        if next_link:
            yield scrapy.Request("http://52.25.87.215/CCGAA/" + next_link, callback=self.parse_detail)
