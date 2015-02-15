#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from urlparse import urlparse

url = 'http://www.wlaimai.com/index.php;param?app=search&cate_id=12#frag'
parsed = urlparse(url)
print parsed