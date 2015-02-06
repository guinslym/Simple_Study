#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import pyqrcode

url = pyqrcode.create('http://www.wlaimai.com')
url.svg('/home/tim/wlaimai.svg',scale=10)