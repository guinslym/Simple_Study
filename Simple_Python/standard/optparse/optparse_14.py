#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import optparse

def with_callback(option,opt_str,value,parser):
    print 'with_callback:'
    print '\toption:',repr(option)
    print '\topt_str:',opt_str
    print '\tvalue:',value
    print '\parser:',parser
    return

parser = optparse.OptionParser()
parser.add_option('--with',
                            action='callback',
                            callback=with_callback,
                            type='string',
                            nargs=2,
                            help='Include optional feature')
parser.parse_args(['--with','foo','bar'])