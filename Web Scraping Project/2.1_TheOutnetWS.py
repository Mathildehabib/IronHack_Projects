# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:16:24 2019

@author: mathi
"""

import requests as r
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import time as t


def table_generator(url_pattern,pages_to_scrape):
    table=[]
    for i in range(1,pages_to_scrape+1):
        if i%2==0:
            t.sleep(2)
        url=url_pattern%i
        lst=BS(r.get(url).content).select('div.description>span.designer-name,span.discounted>span.value,span.full>span.value,div.description>span.title')
        table_url=[(j.text).strip('\r\n\txa').replace('\xa0','') for j in lst]
        table+=table_url
    return table

def cleaner(table):
    table_2=[]
    table_3=[]
    for i in range((len(table)-1)):
        if table[i]!=table[i+1]:
            table_2.append(table[i])
    table_2.append(table[-1])
    for i in range(0,(len(table_2)-1)):
        if i==0:
            table_3.append(table_2[i])
        elif (table_2[i].isdigit()) & (table_2[i+1].isdigit()==False) & (table_2[i-1].isdigit()==False):
            table_3.append(table_2[i])
            table_3.append('')
        else:
            table_3.append(table_2[i])
    table_3.append(table_2[-1])
    return table_3

def columns(clean_table):
    Brand=[clean_table[i].upper() for i in range(0,len(clean_table),4)]
    SalePrice=[clean_table[i] for i in range(1,len(clean_table),4)]
    OriginalPrice=[clean_table[i] for i in range(2,len(clean_table),4)]
    Description=[clean_table[i] for i in range(3,len(clean_table),4)]
    return Brand,Description,SalePrice,OriginalPrice

def web_scraper(url_pattern,pages_to_scrape):
    table=table_generator(url_pattern,pages_to_scrape)
    clean_table=cleaner(table)
    Brand,Description,SalePrice,OriginalPrice=columns(clean_table)    
    return Brand,Description,SalePrice,OriginalPrice