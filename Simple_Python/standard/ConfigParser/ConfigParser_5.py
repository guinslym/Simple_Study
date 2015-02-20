#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')
for candidate in ['wiki','bug_tracker','dvcs']:
    print '%-12s:%s' % (candidate,parser.has_section(candidate))