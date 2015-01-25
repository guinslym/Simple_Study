#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
import sys
from codecs_1 import to_hex

text = ''.join(map(chr,range(97,123)))+'\n'
repetitions =50

print 'Text length :',len(text)
print 'Repetitions :',repetitions
print 'Expected len:',len(text) * repetitions

# Encode the text serveral times to build up a large amount of data
encoder = codecs.getincrementalencoder('bz2')()
encoded= []

print
print 'Encoding:',
for i in range(repetitions):
    en_c = encoder.encode(text,final=(i==repetitions-1))
    if en_c:
        print '\nEncoded : {} bytes'.format(len(en_c))
        encoded.append(en_c)
    else:
        sys.stdout.write('.')

bytes = ''.join(encoded)
print
print 'Total encoded length:',len(bytes)
print

# Decoded the byte string one byte at a time
decoder = codecs.getincrementaldecoder('bz2')()
decoded = []

print 'Decoding:',
for i,b in enumerate(bytes):
    final = (i+1) == len(text)
    c = decoder.decode(b,final)
    if c:
        print '\nDecoded :{} characters'.format(len(c))
        print 'Decoding:',
        decoded.append(c)
    else:
        sys.stdout.write('.')
print
restored = u''.join(decoded)

print
print 'Total uncompressed length:',len(restored)