#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
TEST_GID=100
TEST_UID=1000

def show_user_info():
    print 'Use (actual/effective) : %d / %d' % (os.getuid(),os.geteuid())
    print 'Group (actual/effective) : %d / %d' % (os.getgid(),os.getegid())
    print 'Actual Groups :',os.getgroups()
    return

print 'BEFORE CHANGE:'
show_user_info()
print

try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERROR:Could not change effective group.Rerun as root'
else:
    print 'CHANGED GROUP:'
    show_user_info()
    print

try:
    os.seteuid(TEST_UID)
except OSError:
    print 'ERROR:Could not change effective user.Rerun as root.'
    show_user_info()
    print