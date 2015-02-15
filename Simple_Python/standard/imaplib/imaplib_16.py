#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import imaplib_1
from imaplib_4 import parse_list_response

c = imaplib_1.open_connection()
try:
    c.select('Archive.Today')
    #What ids are in the mailbox
    typ,[msg_ids] = c.search(None,'ALL')
    print 'Starting message:',msg_ids

    # Find the message(s)
    typ,response = c.search(None,'(SUBJECT "test")')
    msg_ids = ','.join(msg_ids.split(' '))
    print 'Matching messages:',msg_ids

    # What are the current flags?
    typ,response = c.fetch(msg_ids,'(FLAGS)')
    print 'Flags before:',response

    # Change the Deleted flag
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')

    # What are the flags now?
    typ,response = c.fetch(msg_ids,'(FLAGS)')
    print 'Flags after:',response

    # Really delete the message
    typ,response = c.expunge()
    print 'Expunged:',response

    # What ids are left in the mailbox?
    typ,[msg_ids] = c.search(None,'ALL')
    print 'Remaining messages:',msg_ids
finally:
    try:
        c.close()
    except:
        pass
    c.logout()