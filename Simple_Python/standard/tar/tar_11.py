#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from cStringIO import StringIO
from contextlib import closing

data = 'This is the data to write to the archive.'

with closing(tarfile.open('addfile_string.tar',mode='w')) as out:
    info = tarfile.TarInfo('made_up_file.txt')
    info.size = len(data)
    out.addfile(info,StringIO(data))

print 'Contents:'
with closing(tarfile.open('addfile_string.tar',mode='r')) as t:
    for member_info in t.getmembers():
        print member_info.name
        f = t.extractfile(member_info)
        print f.read()