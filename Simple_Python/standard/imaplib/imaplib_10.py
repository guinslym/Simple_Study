#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import imaplib_1
from imaplib_4 import parse_list_response

c = imaplib_1.open_connection()
try:
    typ, mailbox_data = c.list()
    for line in mailbox_data:
        flags, delimiter, mailbox_name = parse_list_response(line)
        c.select(mailbox_name, readonly=True)
        typ, msg_ids = c.search(None, 'ALL')
        print mailbox_name, typ, msg_ids
finally:
    try:
        c.close()
    except:
        pass
    c.logout()