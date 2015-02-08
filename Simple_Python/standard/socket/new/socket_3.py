#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import socket

for host in ['www.python.org','www.wlaimai.com','yafeile.koding.io','nosuchname']:
    print host
    try:
        hostname,aliases,addresses = socket.gethostbyname_ex(host)
        print 'Hostname:',hostname
        print 'Aliases     :',aliases
        print 'Addresses:',addresses
    except socket.error as msg:
        print 'ERROR:',msg
    print