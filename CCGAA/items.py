# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcgaaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cell_line = scrapy.Field()
    primary_site = scrapy.Field()
    atcc_annotation = scrapy.Field()
    eigenstrat = scrapy.Field()
