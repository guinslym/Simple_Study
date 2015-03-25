#! /usr/bin/python

# HTTP Header
print "Content-Type:application/octet-stream;name=\"FileName\"\r\n";
print "Content-Disposition:attachment;filename=\"FileName\"\r\n\n";

# Actual File Content will go hear.
f = open('/home/dog/cgi-bin/tmp/sql.txt','rb')

str = f.read()
print str

# Close opend file
f.close()