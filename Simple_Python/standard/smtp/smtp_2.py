#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

# Prompt the user for connection info
to_email = raw_input('Recipient:')
servername = raw_input('Mail server name:')
username = raw_input('Mail username:')
password = getpass.getpass("%s's password:"%username)

# Create the message
msg = MIMEText('Test message from yafeile')
msg.set_unixfrom('yafeile')
msg['To'] = email.utils.formataddr(('Recipient',to_email))
msg['From'] = email.utils.formataddr(('Yafeile','yafeile@163.com'))
msg['Subject'] = 'Test from smtplib study'
server = smtplib.SMTP(servername)
try:
    server.set_debuglevel(True)
    #identify ourselves,promting server for supported features
    server.ehlo()
    # if we can encrypt this session,do it
    if server.has_extn('STARTTLS'):
        server.starttls()
        server.ehlo() #reidentify ourselves over TLS connection
    server.login(username,password)
    server.sendmail('yafeile@163.com',
                            [to_email],
                            msg.as_string())
except smtplib.SMTPSenderRefused:
    print 'ERROR:can not send to the recipient address'
finally:
    server.quit()