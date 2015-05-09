# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:36:03 2015

@author: tim
"""

import sys
from twisted.python import log

log.startLogging(sys.stdout)
log.msg('Starting experiment')
log.msg('Logging an exception')

try:
    1/0
except ZeroDivisionError,e:
    log.err(e)

log.msg('Ending experiment')