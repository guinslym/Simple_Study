#! /usr/bin/python

import cgi,cgitb
from os import environ
import string

if environ.has_key('HTTP_COOKIE'):
	data = environ['HTTP_COOKIE']
	for cookie in map(data.strip,data.split(';')):
		(key,value) = cookie.split('=')
		if key=='user_id':
			user_id = value
		if key=='password':
			password = value
		else:
			password = ''

print 'User ID = %s' % user_id
print 'Password = %s' % password