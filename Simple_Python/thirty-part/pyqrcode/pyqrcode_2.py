#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import pyqrcode

big_code = pyqrcode.create('http://www.wlaimai.com',error='L',version=10)
big_code.png('/home/tim/code.png',scale=6,module_color=[0,0,0,128],background=[0xff,0xff,0xff])