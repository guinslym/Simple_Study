#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox

mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
    to_remove = []
    for key,msg in mbox.iteritems():
        if '2' in msg['subject']:
            print 'Removing:',key
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()