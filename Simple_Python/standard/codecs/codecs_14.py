#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
import sys
import locale

# Configure locale from the user's environment settings.
locale.setlocale(locale.LC_ALL,'')

# Wrap stdout with an encoding-aware writer
lang,encoding = locale.getdefaultlocale()
sys.stdin = codecs.getreader(encoding)(sys.stdin)

print 'From stdin:'
print repr(sys.stdin.read())