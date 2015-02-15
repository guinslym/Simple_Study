#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import pprint
import imaplib_1

c = imaplib_1.open_connection()
try:
    c.select('INBOX',readonly=True)
    print 'HEADER:'
    typ,msg_data = c.fetch('1','(BODY.PEEK[HEADER])')
    for response_part in msg_data:
        if isinstance(response_part,tuple):
            print response_part[1]
    print 'BODY TEXT:'
    typ,msg_data = c.fetch('1','(BODY.PEEK[TEXT])')
    for response_part in msg_data:
        if isinstance(response_part,tuple):
            print response_part[1][0:100]
    print '\nFLAGS:'
    typ,msg_data = c.fetch('1','(FLAGS)')
    for response_part in msg_data:
        print response_part
        print imaplib.ParseFlags(response_part)

finally:
    try:
        c.close()
    except Exception, e:
        print e
    c.logout()