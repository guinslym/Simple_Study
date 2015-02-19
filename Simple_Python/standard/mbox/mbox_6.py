#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox
import os

mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    to_remove = []
    for key,msg in mbox.iteritems():
        if '2' in msg['subject']:
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

for dirname,subdirs,files in os.walk('Example'):
    print dirname
    print '\tDirectories:',subdirs
    for name in files:
        fullname = os.path.join(dirname,name)
        print
        print '*'*3,fullname
        print open(fullname).read()
        print '*'*20