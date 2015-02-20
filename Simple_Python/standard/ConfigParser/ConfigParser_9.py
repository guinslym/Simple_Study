#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker','uri','http://localhost:8080/bugs')
parser.set('bug_tracker','username','Jack')
parser.set('bug_tracker','password','123456')

for section in parser.sections():
    print section
    for name,value in parser.items(section):
        print ' %s = %r' % (name,value)