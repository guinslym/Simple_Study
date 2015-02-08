#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import socket
for host in ['locahost','127.0.0.1:81']:
    print '%6s :%s' % (host,socket.getfqdn(host))