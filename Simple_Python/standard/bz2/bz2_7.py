#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2
import os
import contextlib
import itertools

with contextlib.closing(bz2.BZ2File('lines.bz2','wb')) as output:
    output.writelines(
        itertools.repeat('This same line,over and over,\n',10))
os.system('bzcat lines.bz2')