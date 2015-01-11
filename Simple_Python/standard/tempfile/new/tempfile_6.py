#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tempfile

with tempfile.NamedTemporaryFile(suffix='_suffix',prefix='prefix_',dir='/tmp',) as temp:
    print 'temp:'
    print ' ',temp
    print 'temp.name:'
    print ' ',temp.name