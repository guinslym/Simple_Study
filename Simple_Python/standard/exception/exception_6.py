#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import math
import fpectl

print 'Control off:',math.exp(1000)
fpectl.turnon_sigfpe()
print 'Control on:',math.exp(1000)