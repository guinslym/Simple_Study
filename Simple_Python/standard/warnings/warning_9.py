#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import warnings
import logging

logging.basicConfig(level=logging.INFO)

def send_warning_to_log(message,category,filename,lineno,file=None):
    logging.warning(
        '%s:%s: %s:%s' %
        (filename,lineno,category.__name__,message))
    return
old_showwarning = warnings.showwarning
warnings.showwarning = send_warning_to_log
warnings.warn('message')