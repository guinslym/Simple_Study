# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import Cookie

c = Cookie.SimpleCookie()
c['integer'] = 5
c['string_with_quotes'] = 'He said,"Hello,World!"'

for name in ['integer','string_with_quotes']:
	print c[name].key
	print ' %s'%c[name]
	print ' value=%r'%c[name].value
	print ' coded_value=%r'%c[name].coded_value
	print