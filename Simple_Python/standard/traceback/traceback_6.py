#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
from traceback_1 import call_function

def f():
    traceback.print_stack(file=sys.stdout)
print 'Calling f() directly:'
f()

print
print 'Calling f() from 3 levels deep:'
call_function(f)