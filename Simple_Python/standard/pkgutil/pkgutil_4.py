#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import nested
import nested.shallow

print 'nested.shallow:',nested.shallow.__file__
nested.shallow.func()

print
import nested.second.deep
print 'nested.second.deep:',nested.second.deep.__file__
nested.second.deep.func()