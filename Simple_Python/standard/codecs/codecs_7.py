#! /us/bin/env/python
# -*- coding:utf-8 -*-

from codecs_1 import to_hex
import codecs

# Pick the nonnative version of UTF-16 encoding
if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'

print 'Native order :',to_hex(codecs.BOM_UTF16,2)
print 'Selected order :',to_hex(bom,2)

# Encode the text.
encoded_text = u'pi: \u03c0'.encode(encoding)
print '{:14} : {}'.format(encoding,to_hex(encoded_text,2))

with open('nonnative-encoded.txt',mode='wb') as f:
    # Write the selected byte-order marker.It is not included
    # in the encoded text because the byte order was given
    # explicitly when selecting the encoding.
    f.write(bom)
    # Write the byte string for the encoded text
    f.write(encoded_text)