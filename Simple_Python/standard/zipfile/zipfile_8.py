#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile
from zipfile_3 import print_info

with zipfile.ZipFile('write_arcname.zip',mode='w') as zf:
    zf.write('file.csv',arcname='NOT_README.csv')
print_info('write_arcname.zip')