#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import asyncore
import logging
import socket

from asynchat_2 import EchoHandler

class EchoServer(asyncore.dispatcher):
    """Receives connections and establishes handlers for each client."""
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)
        return

    def handle_accept(self):
        # Called when a client connects to our socket
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        # Only deal with one client at a time,
        # so close as soon as the handler is set up.
        # Under normal conditions, the server
        # would run forever or until it received
        # instructions to stop.
        self.handle_close()
        return
    def handle_close(self):
        self.close()