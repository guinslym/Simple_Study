#! /us/bin/env/python
# -*- coding:utf-8 -*-

from codecs_1 import to_hex
import codecs

for name in ['BOM','BOM_BE','BOM_LE',
                   'BOM_UTF8',
                   'BOM_UTF16','BOM_UTF16_BE','BOM_UTF16_LE',
                   'BOM_UTF32','BOM_UTF32_BE','BOM_UTF32_LE',
                  ]:
    print '{:12} : {}'.format(name,to_hex(getattr(codecs,name),2))