#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile
from zipfile_3 import print_info

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = {
    zipfile.ZIP_DEFLATED:'deflated',
    zipfile.ZIP_STORED:'stored',
}

print 'creating archive'
with zipfile.ZipFile('write_compression.zip',mode='w') as zf:
    mode_name = modes[compression]
    print 'adding file webservice with compression mode,mode_name'
    zf.write('webservice',compress_type=compression)
print
print_info('write_compression.zip')