#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
import time
from contextlib import closing

with closing(tarfile.open('example.tar','r')) as t:
    for member_info in t.getmembers():
        print member_info.name
        print '\tModified:\t',time.ctime(member_info.mtime)
        print '\tMode    :\t',oct(member_info.mode)
        print '\tType     :\t',member_info.type
        print '\tSize      :\t',member_info.size,'bytes'
        print