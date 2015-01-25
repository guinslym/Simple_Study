#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
from cStringIO import StringIO
from codecs_1 import to_hex

buffer = StringIO()
stream = codecs.getwriter('zlib')(buffer)
text = (''.join(map(chr,range(97,123)))+'\n')*50

stream.write(text)
stream.flush()

print 'Original length:',len(text)
compressed_data =buffer.getvalue()
print 'ZIP compressed :',len(compressed_data)

buffer = StringIO(compressed_data)

stream = codecs.getreader('zlib')(buffer)

first_line = stream.readline()
print 'Read first line :',repr(first_line)

uncompressed_data = first_line + stream.read()
print 'Uncompressed :',len(uncompressed_data)
print 'Same               :',text == uncompressed_data