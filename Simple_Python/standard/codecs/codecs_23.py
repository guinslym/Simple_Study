#! /us/bin/env/python
# -*- coding:utf-8 -*-

from codecs_22 import encoding_map
import codecs

text = u"pi:π"

for error in ['ignore','replace','strict']:
    try:
        encoded = codecs.charmap_encode(text,error,encoding_map)
    except UnicodeEncodeError, e:
        encoded = str(e)
    print '{:7} : {}'.format(error,encoded)