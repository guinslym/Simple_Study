#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker','url','http://%(server)s:%(port)s/bugs')

try:
    print parser.get('bug_tracker','url')
except ConfigParser.InterpolationMissingOptionError, err:
    print 'ERROR:',err