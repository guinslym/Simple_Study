#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('interpolation_default.ini')

print 'URL:',parser.get('bug_tracker','url')