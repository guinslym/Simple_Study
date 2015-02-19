#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import mailbox
import os

def show_maildir(name):
    os.system('find %s -print' % name)
mbox = mailbox.Maildir('Example')
print 'Before:',mbox.list_folders()
show_maildir('Example')

print
print '*'*30
print

mbox.add_folder('subfolder')
print 'subfolder created:',mbox.list_folders()
show_maildir('Example')

subfolder = mbox.get_folder('subfolder')
print 'subfolder contents:',subfolder.list_folders()

print
print '*'*30
print

subfolder.add_folder('second_level')
print 'second_level created:',subfolder.list_folders()
show_maildir('Example')

print
print '#'*30
print

subfolder.remove_folder('second_level')
print 'second_level removed:',subfolder.list_folders()
show_maildir('Example')