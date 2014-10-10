#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import socket

def get_remote_machine_info():
    remote_host='www.itcast.cn'

    try:
        print "IP address:{}".format(socket.gethostbyname(remote_host))

    except socket.error, socket.errno:
        print "{error},{errno}".format(error=socket.error,errno=socket.errno)

if __name__ == '__main__':
    get_remote_machine_info()

