#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tempfile

tempfile.tempdir = '/I/changed/this/path'
print 'gettempdir():',tempfile.gettempdir()