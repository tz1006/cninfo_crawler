#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: crawler.py
# version: 0.0.1
# description: crawler.py


import requests



url = 'http://www.cninfo.com.cn/new/singleDisclosure/fulltext?stock=600053&pageSize=20&pageNum=3&tabname=latest&plate=sse&limit='


with requests.Session() as s:
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    r = s.post(url, data=payload)
