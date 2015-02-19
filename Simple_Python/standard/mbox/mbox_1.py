#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox
import email.utils

from_addr = email.utils.formataddr(('Author',
                                                         'author@example.com'))
to_addr = email.utils.formataddr(('Recipient',
                                                     'recipient@example.com'))
mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb 7 10:23:12 2012')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 1'
    msg.set_payload('\n'.join(['This is the body.',
                                              'From (should be escaped).',
                                              'There are 3 lines.\n',
                                              ]))
    mbox.add(msg)
    mbox.flush()
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 2'
    msg.set_payload('This is the second body.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print open('example.mbox','r').read()