# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:39:06 2019

@author: mathi
"""

import requests as r
from bs4 import BeautifulSoup as BS
import pandas as pd
import re
import time as t

def table_generator(url_pattern,headers,pages_to_scrape):
    table_brand=[]
    table_price=[]
    for i in range(1,pages_to_scrape+1):
        if i%2==0:
            t.sleep(2)
        url=url_pattern%i
        soup=BS(r.get(url,headers=headers).content)
        lst1=soup.select('a>span.designer')
        table_url1=[(j.text).upper() for j in lst]
        table_brand+=table_url1
        lst2=soup.select('span.price')
        table_url2=[(k.text).strip('\n\t€').replace(',','') for k in lst]
        table_price+=table_url2
     
    return table_brand, table_price
