#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile
from zipfile_3 import print_info

print 'creating archive'
with zipfile.ZipFile('append.zip',
                             mode='w',
                             ) as zf:
    zf.write('file.csv')
print
print_info('append.zip')

print 'appending to the archive'
with zipfile.ZipFile('append.zip',mode='a') as zf:
    zf.write('webservice',arcname='hello')
print
print_info('append.zip')