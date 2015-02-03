#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile
from zipfile_3 import print_info

print 'creating archive'
with zipfile.ZipFile('write.zip',mode='w') as zf:
    print 'adding file webservice'
    zf.write('webservice')
print
print_info('write.zip')