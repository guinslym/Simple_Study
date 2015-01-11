#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tempfile
import os

with tempfile.NamedTemporaryFile() as temp:
    print 'temp:'
    print ' ',temp
    print 'temp.name:'
    print ' ',temp.name

print 'Exists after close:',os.path.exists(temp.name)