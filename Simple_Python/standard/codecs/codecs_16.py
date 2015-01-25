#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
from cStringIO import StringIO

buffer = StringIO()
stream = codecs.getwriter('rot-13')(buffer)

text = ''.join(map(chr,range(97,123)))

stream.write(text)
stream.flush()

print 'Original:',text
print 'ROT-13 :',buffer.getvalue()