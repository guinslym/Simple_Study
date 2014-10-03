import tarfile
from contextlib import closing

print "Creating archive"
with closing(tarfile.open("test.tar",mode="w")) as out:
    out.add("test.txt")

print "contents:",
with closing(tarfile.open("test.tar",mode="r")) as t:
    print [m.name for m in t.getmembers()]

print "adding index.rst"
with closing(tarfile.open("test.tar",mode="a")) as out:
    out.add("weather.xml")

print "contents:"
with closing(tarfile.open("test.tar",mode="r")) as t:
    print [m.name for m in t.getmembers()]
