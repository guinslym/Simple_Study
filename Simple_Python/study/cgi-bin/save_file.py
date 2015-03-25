#! /usr/bin/python

import cgi,cgitb
import os

cgitb.enable()

form = cgi.FieldStorage()

# Get filename here
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
	fn = os.path.basename(fileitem.filename.replace("\\","/"))
	open('/home/dog/cgi-bin/tmp/'+fn,'wb').write(fileitem.file.read())
	message = 'This file '+fn+' was uploaded successfully'
else:
	message = 'No file was uploaded'

print """Content-Type:text/html\r\n
<html>
<body>
<p>%s</p>
</body>
</html>
""" % (message)