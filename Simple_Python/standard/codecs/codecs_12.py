#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
import sys

text = u'pi:π'

# Wrap sys.stdout with a writer that knows
#how to handle encoding Unicode data
wrapped_stdout = codecs.getwriter('UTF-8')(sys.stdout)
wrapped_stdout.write(u'Via writer:'+text+'\n')

# Replace sys.stdout with a writer
sys.stdout = wrapped_stdout

print u'Via print :',text