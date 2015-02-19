#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-s',action='store',
                                   dest='simple_value',
                                   help='Store a simple value')
parse.add_argument('-c',action='store_const',
                                   dest='constant_value',
                                   const='value-to-store',
                                   help='Store a constant value')
parse.add_argument('-t',action='store_true',
                                   default='boolean_switch',
                                   help='Set a switch a true')
parse.add_argument('-f',action='store_false',
                                   default=False,
                                   dest='boolean_switch',
                                   help='Set a switch to false')
parse.add_argument('-a',action='append',
                                   dest='collection',
                                   default=[],
                                   help='Add repeated values to a list')
parse.add_argument('-A',action='append_const',
                                   dest='const_collection',
                                   const='value-1-to-append',
                                   default=[],
                                   help='Add different values to list')
parse.add_argument('-B',action='append_const',
                                   dest='const_collection',
                                   const='value-2-to-append',
                                   help='Add different values to list')
parse.add_argument('--version',action='version',
                                   version='%(prog)s 1.0')
results = parse.parse_args()
print 'simple_value = %r' % results.simple_value
print 'constant_value = %r' % results.constant_value
print 'boolean_switch = %r' % results.boolean_switch
print 'collection = %r' % results.collection
print 'const_collection = %r' % results.const_collection