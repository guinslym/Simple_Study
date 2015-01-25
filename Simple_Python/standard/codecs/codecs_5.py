#! /us/bin/env/python
# -*- coding:utf-8 -*-

from codecs_1 import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print 'Reading from',filename
with codecs.open(filename,mode='rt',encoding=encoding) as f:
    print repr(f.read())