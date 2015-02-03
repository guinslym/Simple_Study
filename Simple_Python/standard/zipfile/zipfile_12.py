#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import zipfile
import sys

if __name__ == "__main__":
    with zipfile.PyZipFile("pyzipfile.zip",mode="w") as zf:
        zf.debug=3
        print "Adding python files..."
        zf.writepy(".")
    for name in zf.namelist():
        print name

    print
    sys.path.insert(0,"pyzipfile,zip")
    import zipfile_3
    print "Imported from:",zipfile_3.__file__