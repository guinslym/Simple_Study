#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
from traceback_1 import produce_exception

print 'print_exc() with no exception:'
traceback.print_exc(file=sys.stdout)
print

try:
    produce_exception()
except Exception, err:
    print 'print_exc():'
    traceback.print_exc(file=sys.stdout)
    print
    print 'print_exc(1):'
    traceback.print_exc(limit=1,file=sys.stdout)