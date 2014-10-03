import linecache
from tempfile_1 import *

filename=make_tempfile()
not_there=linecache.getline(filename,50)
print "Not there:%r include %d charcaters"%(not_there,len(not_there)) 
