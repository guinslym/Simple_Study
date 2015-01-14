#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

print 'Testing:',__file__
print 'Exists:',os.access(__file__,os.F_OK)
print 'Readable:',os.access(__file__,os.F_OK)
print 'Writable:',os.access(__file__,os.F_OK)
print 'Executable:',os.access(__file__,os.F_OK)