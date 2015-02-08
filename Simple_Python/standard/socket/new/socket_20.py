#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost',10000)
message = 'This is the message.It will be repeated.'

try:
    # Send data
    print >>sys.stderr,'sending "%s"'%message
    send = sock.sendto(message,server_address)

    # Receive response
    print >>sys.stderr,'waiting to receive'
    data,server = sock.recvfrom(4096)
    print >>sys.stderr,'received "%s"' % data
finally:
    print >>sys.stderr,'closing socket'
    sock.close()