#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import re
from imaplib_1 import open_connection

list_response_pattern = re.compile(
                    r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)'
                    )
def parse_list_response(line):
    match = list_response_pattern.match(line)
    flags,delimiter,mailbox_name = match.groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags,delimiter,mailbox_name)

if __name__ == '__main__':
    c = open_connection()
    try:
        typ,data = c.list()
    finally:
        c.logout()
    print 'Response code:',typ
    for line in data:
        print 'Server response:',line
        flags,delimiter,mailbox_name = parse_list_response(line)
        print 'Parsed response:',(flags,delimiter,mailbox_name)