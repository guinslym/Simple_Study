#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from contextlib import closing

print 'creating archive'
with closing(tarfile.open('tarfile_append.tar',mode='w')) as out:
    out.add('untitled')
    out.add('py')

print 'contents:'
with closing(tarfile.open('tarfile_append.tar',mode='r')) as t:
    print [m.name for m in t.getmembers()]

print 'adding file webservice'
with closing(tarfile.open('tarfile_append.tar',mode='a')) as out:
    out.add('webservice')

print 'contents:'
with closing(tarfile.open('tarfile_append.tar',mode='r')) as t:
    print [m.name for m in t.getmembers()]