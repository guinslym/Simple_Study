#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import ConfigParser
import sys

parser = ConfigParser.SafeConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker','url','http://localhost:8080/bugs')
parser.set('bug_tracker','username','jack')
parser.set('bug_tracker','password','123456')
parser.write(sys.stdout)