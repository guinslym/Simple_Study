#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
import os

fmt = '%-30s %-10s'
print fmt % ('FILENAME','SIZE')
print fmt % ('file.csv',os.stat('file.csv').st_size)

for filename,write_mode in [
    ('tarfile_compression.tar','w'),
    ('tarfile_compression.tar.gz','w:gz'),
    ('tarfile_compression.tar.bz2','w:bz2'),
   ]:
    out = tarfile.open(filename,mode=write_mode)
    try:
        out.add('webservice')
    finally:
        out.close()
    print fmt % (filename,os.stat(filename).st_size),
    print [m.name for m in tarfile.open(filename,'r:*').getmembers()]