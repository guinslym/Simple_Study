#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import smtpd
import asyncore

server = smtpd.PureProxy(('127.0.0.1',1025),('smtp.163.com',25))
asyncore.loop()