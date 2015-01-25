#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
import sys
from codecs_1 import to_hex

error_handling = sys.argv[1]

text = u'pi:\u03c0'
print 'Original   :',repr(text)

# Save the data with one encoding
with codecs.open('decode_error.txt','w',encoding='utf-16') as f:
    f.write(text)

# Dump the bytes from the file
with open('decode_error.txt','rb') as f:
    print 'File contents:',to_hex(f.read(),1)

# Try to read the data with the wrong encoding
with codecs.open('decode_error.txt','r',
                            encoding='utf-8',
                            errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError, e:
        print 'ERROR:',e
    else:
        print 'Read  :',repr(data)