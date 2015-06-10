#! /usr/bin/env python

from __future__ import print_function
import socket

HOST = '127.0.0.1'
PORT = 50000

print('Start at port',PORT,)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print('Connected by',addr,)

while True:
    data = conn.recv(1024)
    if not data:
        break
    data = 'Server said:'+data
    conn.sendall(data)
conn.close()