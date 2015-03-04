#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
sys.path.insert(0,'zipimport_example.zip')

import os
import example

print example.__file__
print example.__loader__.get_data('example/__init__.py')