#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox

mbox = mailbox.Maildir('Example')
for message in mbox:
    print message['subject']