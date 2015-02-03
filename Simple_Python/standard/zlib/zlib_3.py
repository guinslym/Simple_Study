#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zlib
import binascii

compressor = zlib.compressobj(1)

with open('zlib_1.py','r') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print 'Compressed:%s' % binascii.hexlify(compressed)
        else:
            print 'buffering...'
    remaining = compressor.flush()
    print 'Flushed:%s' % binascii.hexlify(remaining)