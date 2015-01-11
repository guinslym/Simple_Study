#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import resource
import os

soft,hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print 'Soft limit starts as :',soft

resource.setrlimit(resource.RLIMIT_NOFILE,(4,hard))

soft,hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print 'Soft limit changed to :',soft

random = open('/dev/random','r')
print 'random has fd = ',random.fileno()
try:
    null = open('/dev/null','w')
except IOError, err:
    print err
else:
    print 'null has fd = ',null.fileno()