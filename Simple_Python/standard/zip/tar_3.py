import tarfile
from contextlib import closing
import os

os.mkdir("tar")
with closing(tarfile.open("test.tar","r")) as t:
    t.extract("test.txt","tar")
print os.listdir("tar")
