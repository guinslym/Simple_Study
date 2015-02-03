#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from contextlib import closing

with closing(tarfile.open('example.tar','r')) as t:
    print t.getnames()