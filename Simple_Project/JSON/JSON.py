# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:14:44 2015

@author: tim
"""

import json

class JSON(object):
    def encode(self,data,encoding='utf-8'):
        """对JSON数据编码"""
        return json.dumps(data,encoding)
    def decode(self,data,encoding='utf-8'):
        """对JSON数据解码"""
        return json.loads(data,encoding)