#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2
import contextlib
import os

with contextlib.closing(bz2.BZ2File('example.bz2','wb')) as output:
    output.write('contents of the example file go here.\n')

os.system('file example.bz2')