#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import optparse

parser =optparse.OptionParser(
    usage='%prog [options] <arg1> <arg2>[<arg3>...]',
    prog='my_program_name',
    )
parser.add_option('-a',action='store_true',default=False)
parser.add_option('-b',action='store',dest="b")
parser.add_option('-c',action='store',dest='c',type='int')
parser.parse_args()