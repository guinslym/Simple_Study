#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('simple.ini')
print parser.get('bug_tracker','url')