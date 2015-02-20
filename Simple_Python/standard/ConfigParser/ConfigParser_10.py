#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.read('multisection.ini')

print 'Read values:\n'
for section in parser.sections():
    print section
    for name,value in parser.items(section):
        print ' %s=%r' % (name,value)
parser.remove_option('bug_tracker','password')
parser.remove_section('wiki')
print '\nModified values:\n'
for section in parser.sections():
    print section
    for name,value in parser.items(section):
        print ' %s=%r' % (name,value)