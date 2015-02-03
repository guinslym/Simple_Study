#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile

for filename in ['README.txt','example.tar',
                        'bad_example.tar','notthere.tar']:
    try:
        print '%15s %s' % (filename,tarfile.is_tarfile(filename))
    except IOError, e:
        print '%15s %s' % (filename,e)