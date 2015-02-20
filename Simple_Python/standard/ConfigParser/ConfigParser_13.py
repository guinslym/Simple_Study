#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('interpolation.ini')
print 'Original value  :',parser.get('bug_tracker','url')
parser.set('bug_tracker','port','9090')
print 'Altered port value :',parser.get('bug_tracker','url')
print 'Without interpolation:',parser.get('bug_tracker','url',raw=True)