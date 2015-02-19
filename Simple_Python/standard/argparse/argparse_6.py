#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse
from ConfigParser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-a',action='store_true',default=False)
parser.add_argument('-b',action='store',dest='b')
parser.add_argument('-c',action='store',dest='c',type=int)

config = ConfigParser()
config.read('argparse_with_shlex.ini')
config_value = config.get('cli','options')
print 'Config :',config_value

argment_list = shlex.split(config_value)
print 'Arg List:',argment_list
print 'Results:',parser.parse_args(argment_list)