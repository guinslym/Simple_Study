#! /usr/bin/env/python
# -*- coding:utf-8 -*-

print 'Loading sitecustomize.py'

import site
import platform
import os
import sys

path = os.path.join('/opt',
                              'python',
                              sys.version[:3],
                              platform.platform(),
                              )
print 'Adding new path',path
site.addsitedir(path)