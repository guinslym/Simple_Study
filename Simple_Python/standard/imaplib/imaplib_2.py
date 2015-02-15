#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import ConfigParser
import os

# Read the config file
config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/info')])

# Connect to the server
hostname = config.get('server','hostname')
print 'Connecting to',hostname
connection = imaplib.IMAP4_SSL(hostname)

# Login to our account
username = config.get('account','username')
password = 'this_is_the_wrong_password'
print 'Logging in as',username
try:
    connection.login(username,password)
except Exception as err:
    print 'ERROR:',err