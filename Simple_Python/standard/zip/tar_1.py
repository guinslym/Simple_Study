import tarfile
from contextlib import closing

with closing(tarfile.open("test.tar","r")) as t:
             print t.getnames()
