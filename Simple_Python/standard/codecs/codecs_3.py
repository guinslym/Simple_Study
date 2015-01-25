#! /us/bin/env/python
# -*- coding:utf-8 -*-

from codecs_1 import to_hex

text = u'pi:π'
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print 'Original   :',repr(text)
print 'Encoded:',to_hex(encoded,1),type(encoded)
print 'Decoded',repr(decoded),type(decoded)