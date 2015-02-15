#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import imaplib_1

c = imaplib_1.open_connection()
try:
    typ,data = c.select('Does Not Exist')
    print typ,data
finally:
    c.logout()