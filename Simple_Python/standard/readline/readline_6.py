#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import readline

def startup_hook():
    readline.insert_text('from start up_hook')
def pre_input_hook():
    readline.insert_text('from pre_input_hook')
    readline.redisplay()

readline.set_startup_hook(startup_hook)
readline.set_pre_input_hook(pre_input_hook)
readline.parse_and_bind('tab:complete')

while True:
    line = raw_input('Prompt ("stop" to quit):')
    if line == 'stop':
        break
    print 'ENTERED:"%s"' % line