#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import demopkg
print 'demopkg:',demopkg.__file__

import demopkg.shared
print 'demopkg.shared:',demopkg.shared.__file__

import demopkg.not_shared
print 'demopkg.not_shared:',demopkg.not_shared.__file__