#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import asyncore
import logging
import socket

from asynchat_1 import EchoServer
from asynchat_3 import EchoClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)-11s: %(message)s',
                    )

address = ('localhost', 0) # let the kernel give us a port
server = EchoServer(address)
ip, port = server.address # find out what port we were given

message_data = open('untitled.md', 'r').read()
client = EchoClient(ip, port, message=message_data)

asyncore.loop()