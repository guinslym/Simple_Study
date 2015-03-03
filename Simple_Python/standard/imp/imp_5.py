#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imp
import sys

for i in range(2):
    print i
    try:
        m = sys.modules['example']
    except KeyError:
        print '(not in sys.modules)',
    else:
        print '(have in sys.modules)',
    f,filename,description = imp.find_module('example')
    example_package = imp.load_module('example',f,filename,
                                                                 description)