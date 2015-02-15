#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import smtplib

server = smtplib.SMTP('smtp.163.com')
server.set_debuglevel(True) #show communication with the server
try:
    dhellmann_result = server.verify('dhellmann')
    yafeile_result = server.verify('yafeile')
    zhuzhu_result = server.verify('zhuzhulang')
finally:
    server.quit()
print 'dhellmann:',dhellmann_result
print 'yafeile:',yafeile_result
print 'zhuzhu',zhuzhu_result