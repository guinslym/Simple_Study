#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

SECTIONS = ['wiki','none']
OPTIONS = ['username','password','url','description']

for section in SECTIONS:
    has_section = parser.has_section(section)
    print '%s section exists:%s' % (section,has_section)
    for candidate in OPTIONS:
        has_option = parser.has_option(section,candidate)
        print '%s.%-12s :%s' % (section,
                                           candidate,
                                           has_option,
                                           )
    print