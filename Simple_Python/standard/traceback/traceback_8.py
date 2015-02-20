#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
import os
from traceback_1 import call_function

def f():
    return traceback.extract_stack()

stack = call_function(f)
for filename,linenum,funcname,source in stack:
    print '%-26s:%s "%s" in %s()' % (os.path.basename(filename),
                                                   linenum,
                                                   source,
                                                   funcname)