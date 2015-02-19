#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',metavar='in-file',
                                    type=argparse.FileType('rt'))
parser.add_argument('-o',metavar='out-file',
                                    type=argparse.FileType('wt'))
try:
    result = parser.parse_args()
    print 'Input file:',result.i
    print 'Output file:',result.o
except IOError,msg:
    parser.error(str(msg))