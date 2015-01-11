#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import platform

print 'interpreter:',platform.architecture()
print '/bin/ls     :',platform.architecture('/bin/ls')