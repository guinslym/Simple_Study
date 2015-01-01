#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib2

response = urllib2.urlopen('http://localhost:8000/')
data=[line.rstrip() for line in response]
for d in data:
    print d