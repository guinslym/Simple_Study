#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
from pprint import pprint
from traceback_1 import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'format_exception():'
    exc_type,exc_value,exc_tb = sys.exc_info()
    pprint(traceback.format_exception(exc_type,exc_value,exc_tb))