#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import optparse
parser = optparse.OptionParser()
parser.add_option('-v',action='count',
                             dest='verbosity',default=1)
parser.add_option('-q',action='store_const',
                             const=0,dest='verbosity')
options,args = parser.parse_args()
print options.verbosity