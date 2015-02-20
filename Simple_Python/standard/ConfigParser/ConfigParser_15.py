#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.add_section('sect')
parser.set('sect','opt','%(opt)s')

try:
    print parser.get('sect','opt')
except ConfigParser.InterpolationDepthError, err:
    print 'ERROR:',err