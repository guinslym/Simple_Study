#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                                     '710642053@qq.com'))
msg['From'] = email.utils.formataddr(('Author',
                                                     'yafeile@163.com'))
msg['Subject'] = 'Simple test message'
server = smtplib.SMTP('smtp.163.com')
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('yafeile@163.com',
                             ['71-642053@qq.com'],
                             msg.as_string())
except smtplib.SMTPSenderRefused:
    print 'can not send to the recipient'
finally:
    server.quit()