#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import socket

hostname,aliases,addresses = socket.gethostbyaddr('127.0.0.1')

print 'Hostname:',hostname
print 'Aliases     :',aliases
print 'Addresses:',addresses