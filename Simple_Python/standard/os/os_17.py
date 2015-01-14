#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

pid = os.fork()

if pid:
    print 'Child process id:',pid
else:
    print 'I am the child'