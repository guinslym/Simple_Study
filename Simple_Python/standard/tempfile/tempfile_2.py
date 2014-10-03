import linecache
from tempfile_1 import *

filename=make_tempfile()
print "SOURCE:"
print "%r"% data.split("\n")
print
print "CACHE:"
print "%r"% linecache.getline(filename,5)
