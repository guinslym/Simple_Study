#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox
import email.utils
import os

from_addr =email.utils.formataddr(('Author',
                                                         'author@example.com'))
to_addr = email.utils.formataddr(('Recipient',
                                                    'recipient@example.com'))
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb 16 12:23:43 2012')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] ='Sample message 1'
    msg.set_payload('\n'.join(['This is the body.',
                                              'From (will not be escaped).',
                                              'There are 3 lines.\n',
                                              ]))
    mbox.add(msg)
    mbox.flush()
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb 7 12:26:38 2013')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 2'
    msg.set_payload('This is the second body.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

for dirname,subdirs,files in os.walk('Example'):
    print dirname
    print '\tDirectories:',subdirs
    for name in files:
        fullname = os.path.join(dirname,name)
        print
        print '***',fullname
        print open(fullname).read()
        print '*'*20