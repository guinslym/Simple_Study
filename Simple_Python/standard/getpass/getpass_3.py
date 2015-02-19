#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print 'You entered:',p