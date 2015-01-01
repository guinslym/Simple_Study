#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib

url = 'http://localhost:80/~dhellmann/'
print 'urlencode()   :',urllib.urlencode({'url':url})
print 'quote()         :',urllib.quote(url)
print 'quote_plus   :',urllib.quote_plus(url)