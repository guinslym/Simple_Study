#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tarfile
from contextlib import closing

with closing(tarfile.open("example.tar","r")) as t:
    for filename in ["test.txt","file.csv"]:
        try:
            f=t.extractfile(filename)
        except KeyError:
            print "Error;Did not find %s in tar archive" % filename
        else:
            print filename
            print "-"*15
            print f.read()