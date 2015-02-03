#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from contextlib import closing

print 'creating archive'
with closing(tarfile.open('tarfile_add.tar',mode='w')) as out:
    print 'adding file.csv as data.csv'
    info = out.gettarinfo('file.csv',arcname='data.csv')
    out.addfile(info)

print
print 'Contents:'
with closing(tarfile.open('tarfile_add.tar',mode='r')) as t:
    for member_info in t.getmembers():
        print member_info.name