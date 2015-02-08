#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import socket

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                       for n in dir(socket)
                       if n.startswith(prefix)
                       )
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.wlaimai.com','http',
                                                     socket.AF_INET,    #family
                                                     socket.SOCK_STREAM, #socktype
                                                     socket.IPPROTO_TCP, #protocol
                                                     socket.AI_CANONNAME, #flags
                                                     ):
    # Unpack the response tuple
    family,socktype,proto,cannonname,sockaddr = response
    print 'Family    :',families[family]
    print 'Type       :',types[socktype]
    try:
        print 'Protocol  :',protocols[proto]
    except KeyError, e:
        print e
    print 'Canonical name:',cannonname
    print 'Socket address:',sockaddr
    print