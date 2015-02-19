#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import optparse
parser = optparse.OptionParser()
parser.add_option('--earth',action='store_const',
                              const='earth',dest='element',
                              default='earth',
                              )
parser.add_option('--air',action='store_const',
                             const='air',dest='element',
                             )
parser.add_option('--water',action='store_const',
                             const='water',dest='element',
                             )
parser.add_option('--fire',action='store_const',
                             const='fire',dest='element',
                             )
options,args = parser.parse_args()
print options.element