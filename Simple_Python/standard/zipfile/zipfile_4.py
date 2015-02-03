#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile

with zipfile.ZipFile('test.zip') as f:
    for filename in ['webservice','py']:
        try:
            info = f.getinfo(filename)
        except KeyError:
            print 'ERROR:Did not find %s in zip file' % filename
        else:
            print '%s is %d bytes' % (info.filename,info.file_size)