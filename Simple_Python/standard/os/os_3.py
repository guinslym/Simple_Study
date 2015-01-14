#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

print 'Starting:',os.getcwd()

print 'Moving up one:',os.pardir
os.chdir(os.pardir)

print 'After move:',os.getcwd()