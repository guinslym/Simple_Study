# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import logging
import getpass

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
	filename=LOG_FILENAME,
	level=logging.WARNING,
)
logging.warning('The user {0} has not login'.format(getpass.getuser()))

with open(LOG_FILENAME,'rt') as f:
	body = f.read()

print 'FILE:'
print body