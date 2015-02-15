#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import pprint
import imaplib_1

imaplib.Debug = 4
c = imaplib_1.open_connection()
try:
    c.select('INBOX', readonly=True)
    typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER] FLAGS)')
    pprint.pprint(msg_data)
finally:
    try:
        c.close()
    except:
        pass
    c.logout()