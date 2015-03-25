#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print "Content-Type:text/html\n"
if 'user' not in form:
    print 'who are you?'
else:
    print 'Hello,%s' % cgi.escape(form['user'].value)