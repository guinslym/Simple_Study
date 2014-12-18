# -*- coding:utf-8 -*-
# /usr/bin/env/python

import Cookie
HTTP_COOKIE = ';'.join([
	r'integer=5',
	r'string_with_quotes="He said, \"Hello,World!\""',
])
print "From constructor:"
c = Cookie.SimpleCookie(HTTP_COOKIE)
print c
print
print 'From load():'
c = Cookie.SimpleCookie()
c.load(HTTP_COOKIE)
print c