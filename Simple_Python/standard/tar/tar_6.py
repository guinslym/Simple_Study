#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
import os
from contextlib import closing

os.mkdir("outdir")
with closing(tarfile.open("example.tar","r")) as t:
    t.extract("file.csv","outdir")
print os.listdir("outdir")