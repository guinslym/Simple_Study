#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(
    description='Example with long option names'
    )
parser.add_argument('count',action='store',type=int)
parser.add_argument('units',action='store')
print parser.parse_args()