#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os.path

for user in ['','dhellmann','postgresql']:
    lookup = '~'+user
    print '%12s :%s' % (lookup,os.path.expanduser(lookup))