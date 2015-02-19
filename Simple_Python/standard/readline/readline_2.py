#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import readline

readline.read_init_file('myreadline.rc')
while True:
    line = raw_input('Prompt ("stop" to quit):')
    if line == 'stop':
        break
    print 'ENTERED:"%s"' % line