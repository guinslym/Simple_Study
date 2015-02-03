#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile

with zipfile.ZipFile('test.zip') as f:
    for filename in ['webservice','py']:
        try:
            info = f.read(filename)
        except KeyError:
            print 'ERROR:Did not find %s in zip file' % filename
        else:
            print filename,':'
            print info