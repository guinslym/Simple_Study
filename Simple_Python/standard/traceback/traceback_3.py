#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
from traceback_1 import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'print_exception():'
    exc_type,exc_value,exc_tb = sys.exc_info()
    traceback.print_exception(exc_type,exc_value,exc_tb)