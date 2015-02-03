#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
import os
import os.path
from contextlib import closing

if not os.path.exists('outdir'):
    os.mkdir("outdir")
with closing(tarfile.open("example.tar","r")) as t:
    t.extractall("outdir",
                     members=[t.getmember('file.csv')],
                     )
print os.listdir("outdir")