#! /usr/bin/env python

from __future__ import print_function
import socket
import sys

HOST = '127.0.0.1'
PORT = 50000

print('Connect to port',PORT,)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    s.sendall(raw_input('I say:'))
    data = s.recv(1024)
    print('Received',repr(data))
    if not data:
        break
s.close()