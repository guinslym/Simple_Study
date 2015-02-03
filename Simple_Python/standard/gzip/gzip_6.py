#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gzip
from cStringIO import StringIO
import binascii

uncompressed_data = 'This same line,over and over.\n'*10
print 'UNCOMPRESSED:',len(uncompressed_data)
print uncompressed_data

buf = StringIO()
with gzip.GzipFile(mode='wb',fileobj=buf) as f:
    f.write(uncompressed_data)
compressed_data = buf.getvalue()
print 'COMPRESSED:',len(compressed_data)
print binascii.hexlify(compressed_data)

inbuffer = StringIO(compressed_data)
with gzip.GzipFile(mode='rb',fileobj=inbuffer) as f:
    reread_data = f.read(len(uncompressed_data))

print
print 'REREAD:',len(reread_data)
print reread_data