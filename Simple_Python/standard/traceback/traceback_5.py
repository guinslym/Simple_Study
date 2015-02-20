#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
import os
from traceback_1 import produce_exception

try:
    produce_exception()
except Exception, err:
    print 'format_exception()'
    exc_type,exc_value,exc_tb = sys.exc_info()
    for tb_info in traceback.extract_tb(exc_tb):
        filename,linenum,funcname,source = tb_info
        print '%-23s:%s "%s" in %s()' % (os.path.basename(filename),
                                                       linenum,
                                                       source,
                                                       funcname)