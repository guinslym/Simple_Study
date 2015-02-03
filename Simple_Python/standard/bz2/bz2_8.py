#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2
import contextlib

with contextlib.closing(bz2.BZ2File('example.bz2','rb')) as input:
    print input.read()