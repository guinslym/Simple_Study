#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from contextlib import closing

print 'creating archive'
with closing(tarfile.open('tarfile_add.tar',mode='w')) as out:
    print 'adding file:webservice'
    out.add('webservice')

print
print 'Contents:'
with closing(tarfile.open('tarfile_add.tar',mode='r')) as t:
    for member_info in t.getmembers():
        print member_info.name