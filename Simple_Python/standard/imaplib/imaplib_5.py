#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
from imaplib_1 import open_connection

if __name__ == '__main__':
    c = open_connection()
    try:
        typ,data = c.list(directory='Junk E-mail')
    finally:
        c.logout()
    print 'Response code:',typ
    for line in data:
        print 'Server response:',line