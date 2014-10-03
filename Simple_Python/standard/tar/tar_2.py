import tarfile
from contextlib import closing

with closing(tarfile.open("test.tar","r")) as t:
    for filename in ["test.txt"]:
        try:
            f=t.extractfile(filename)
        except KeyError:
            print "Error;Did not find %s in tar archive" % filename
        else:
            print filename
            print "-"*15
            print f.read()
