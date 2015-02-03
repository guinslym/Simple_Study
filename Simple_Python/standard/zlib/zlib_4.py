#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zlib

lorem = open('zlib_1.py','rt').read()
compressed = zlib.compress(lorem)
combined = compressed+lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)
decompressed_matches = decompressed == lorem
print 'Decompressed matches lorem:',decompressed_matches
unused_matches = decompressor.unused_data == lorem
print 'Unused data matches lorem:',unused_matches