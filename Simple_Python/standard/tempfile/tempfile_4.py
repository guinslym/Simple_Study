import linecache
from tempfile_1 import *

filename=make_tempfile()
not_such_file=linecache.getline("1.txt",1)
print "Not there:%r"%not_such_file 
