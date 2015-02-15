#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import re
from imaplib_1 import open_connection
from imaplib_4 import parse_list_response

if __name__ == '__main__':
    c = open_connection()
    try:
        typ,data = c.list()
        for line in data:
            flags,delimiter,mailbox = parse_list_response(line)
            print c.status(
                       mailbox,
                       '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)')
    finally:
        c.logout()