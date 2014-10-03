import fnmatch
import os
import pprint 

pattern="fnmatch_*.py"

files=os.listdir(".")
print
print "Files:"
pprint.pprint(files)

print "-"*20
print "Matches:"
pprint.pprint(fnmatch.filter(files,pattern))
