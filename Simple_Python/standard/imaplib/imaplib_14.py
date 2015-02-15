#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import email.message
import time
import imaplib_1

new_message = email.message.Message()
new_message.set_unixfrom('pymotw')
new_message['Subject'] = 'subject goes here'
new_message['From'] = 'pymotw@example.com'
new_message['To'] = 'example@example.com'
new_message.set_payload('This is the body of the message.\n')
print new_message

c = imaplib_1.open_connection()
try:
    c.append('INBOX','',
        imaplib.Time2Internaldate(time.time()),
        str(new_message))
    # Show the headers for all messages in the mailbox
    c.select('INBOX')
    typ,[msg_ids] = c.search(None,'ALL')
    for num in msg_ids.split():
        typ,msg_data = c.fetch(num,'(BODY.PEEK[HEADER])')
        for response_part in msg_data:
            if isinstance(response_part,tuple):
                print '\n%s:' %num
                print response_part[1]
finally:
    try:
        c.close()
    except Exception, e:
        print e
    c.logout()