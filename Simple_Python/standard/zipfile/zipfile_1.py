#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile

for filename in ['README.txt','example.zip',
                       'bad_exampel.zip','notthere.zip']:
    print '%15s %s' % (filename,zipfile.is_zipfile(filename))