#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',type=int)
parser.add_argument('-f',type=float)
parser.add_argument('--file',type=file)
try:
    print parser.parse_args()
except IOError, msg:
    parser.error(str(msg))