#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import imaplib_1

c = imaplib_1.open_connection()
try:
    # Find the "SEEN" messages in INBOX
    c.select('INBOX')
    typ, [response] = c.search(None, 'SEEN')
    if typ != 'OK':
        raise RuntimeError(response)
    # Create a new mailbox, "Archive.Today"
    msg_ids = ','.join(response.split(' '))
    typ, create_response = c.create('Archive.Today')
    print 'CREATED Archive.Today:', create_response
    # Copy the messages
    print 'COPYING:', msg_ids
    c.copy(msg_ids, 'Archive.Today')
    # Look at the results
    c.select('Archive.Today')
    typ, [response] = c.search(None, 'ALL')
    print 'COPIED:', response
finally:
    c.close()
    c.logout()