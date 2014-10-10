#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import socket

def print_machine_info():
    host_name=socket.gethostname()                            #获取主机名
    ip_address=socket.gethostbyname(host_name)                #获取主机地址
    print "Host name:{0}".format(host_name)                   #利用字典格式化字符串
    print "IP address:{}".format(ip_address)

if __name__ == '__main__':
    print_machine_info()
