#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    print 'Press Return or Ctrl-C:',
    while True:
        ignored = raw_input('say something:')
        print ignored
except Exception, err:
    print 'Caught exception:',err
except KeyboardInterrupt,err:
    print 'Caught KeyboardInterrupt'
else:
    print 'No exception'