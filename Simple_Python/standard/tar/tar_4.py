#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
import time
from contextlib import closing

with closing(tarfile.open('example.tar','r')) as t:
    for filename in ['file.csv']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print 'ERROR:Did not find %s in tar archive' % filename
        else:
            print '%s is %d bytes' % (info.name,info.size)