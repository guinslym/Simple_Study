#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os.path
import os

os.environ['MYVAR'] = 'VALUE'
print os.path.expandvars('/path/to/$MYVAR')