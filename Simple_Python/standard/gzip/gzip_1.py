import gzip
import os
filename="test.txt.gz"
with gzip.open(filename,"wb") as output:
    output.write("Contents of the example of gzip\n")

print filename,"Contain",os.stat(filename).st_size,"bytes"
os.system("file -b --mime %s" % filename)
