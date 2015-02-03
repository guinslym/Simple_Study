#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2
import contextlib

with contextlib.closing(bz2.BZ2File('example.bz2','rb')) as input:
    print 'Entire file:'
    all_data = input.read()
    print all_data

    expected = all_data[5:15]
    # rewind to beginning
    input.seek(0)

    # move ahead 5 bytes
    input.seek(5)
    print 'Starting at position 5 for 10 bytes:'
    partial = input.read(10)
    print partial

    print
    print expected == partial